from collections import Counter
import os
import json
from argparse import ArgumentParser
from random import shuffle

import numpy as np
from sklearn.model_selection import StratifiedKFold

from sklearn.metrics import (
    accuracy_score, 
    balanced_accuracy_score, 
    f1_score, 
    recall_score
)
from transformers import (
    AutoTokenizer,
    Trainer,
    TrainingArguments
)

from glam4cm.data_loading.encoding import EncodingDataset
from glam4cm.models.hf import get_model
from glam4cm.settings import results_dir

def compute_metrics(pred):
    labels = pred.label_ids
    preds = np.argmax(pred.predictions, axis=1)
    acc = (preds == labels).mean()
    f1_macro = f1_score(labels, preds, average='macro')
    accuracy = accuracy_score(labels, preds)
    recall = recall_score(labels, preds, average='macro')
    balanced_acc = balanced_accuracy_score(labels, preds)

    return {
        'balanced_accuracy': balanced_acc,
        'accuracy': acc,
        'f1_macro': f1_macro,
        'precision': accuracy,
        'recall': recall
    }


def get_parser():
    parser = ArgumentParser()
    parser.add_argument('--seed', type=int, default=42)
    parser.add_argument('--dataset_name', type=str, default='ecore_555')
    parser.add_argument('--model_name', type=str, default='bert-base-uncased')
    parser.add_argument('--ckpt', type=str, default=None)
    parser.add_argument('--max_length', type=int, default=512)
    parser.add_argument('--k', type=int, default=10)
    parser.add_argument('--limit', type=int, default=-1)
    parser.add_argument('--trust_remote_code', action='store_true')
    parser.add_argument('--include_dummies', action='store_true')
    parser.add_argument('--task_type', type=str, default='graph_cls')

    parser.add_argument('--num_epochs', type=int, default=10)

    parser.add_argument('--warmup_steps', type=int, default=500)
    parser.add_argument('--num_log_steps', type=int, default=500)
    parser.add_argument('--num_eval_steps', type=int, default=500)
    parser.add_argument('--num_save_steps', type=int, default=500)
    parser.add_argument('--train_batch_size', type=int, default=2)
    parser.add_argument('--eval_batch_size', type=int, default=128)
    parser.add_argument('--lr', type=float, default=1e-5)

    return parser


def run(args):
    dataset_name = args.dataset_name
    model_name = args.model_name
    include_dummies = args.include_dummies
    
    file_name = 'ecore.jsonl' if include_dummies and dataset_name == 'modelset' else 'ecore-with-dummy.jsonl'
    texts = [
        (g['txt'], g['labels'])
        for g in json.load(open(f'datasets/{dataset_name}/{file_name}'))
        if g['labels'] not in ['dummy', 'unknown']
    ]
    allowed_labels = [label for label, _ in dict(Counter([t[1] for t in texts]).most_common(48)).items()]
    texts = [
        (t, l) for t, l in texts
        if l in allowed_labels
    ]
    if args.task_type == 'dd':
        print("Task type: DD")
        texts = [(t, 0 if l in 'dummy' else 1) for t, l in texts]
        
    shuffle(texts)
    limit = args.limit if args.limit > 0 else len(texts)
    texts = texts[:limit]
        
    labels = [y for _, y in texts]
    y_map = {label: i for i, label in enumerate(set(y for y in labels))}
    y = [y_map[y] for y in labels]
    n = len(texts)

    texts = [text for text, _ in texts]

    num_labels = len(y_map)

    tokenizer = AutoTokenizer.from_pretrained(model_name, trust_remote_code=args.trust_remote_code)
    k = args.k
    kfold = StratifiedKFold(n_splits=k, shuffle=True, random_state=args.seed)

    i = 0
    for train_idx, test_idx in kfold.split(np.zeros(n), np.zeros(n)):
        # if i == 0:
        #     continue
        print(f'Fold {i+1}/{k}')

        train_texts = [texts[i] for i in train_idx]
        test_texts = [texts[i] for i in test_idx]
        train_y = [y[i] for i in train_idx]
        test_y = [y[i] for i in test_idx]


        print(f'Train: {len(train_texts)}, Test: {len(test_texts)}', num_labels)

        train_dataset = EncodingDataset(tokenizer, train_texts, train_y, max_length=args.max_length)
        test_dataset = EncodingDataset(tokenizer, test_texts, test_y, max_length=args.max_length)
        # import code; code.interact(local=locals())

        model = get_model(
            args.ckpt if args.ckpt else model_name, 
            num_labels, 
            len(tokenizer), 
            trust_remote_code=args.trust_remote_code
        )

        print("Training model")
        output_dir = os.path.join(
            results_dir,
            dataset_name,
            f'graph_cls_comp_{"dummy" if include_dummies else ""}{i+1}',
        )

        logs_dir = os.path.join(
            'logs',
            f"{dataset_name}_{args.model_name if args.ckpt is None else args.ckpt.split('/')[-1]}",
            f'graph_cls_comp_{"dummy" if include_dummies else ""}{i+1}',
        )

        print("Running epochs: ", args.num_epochs)

        # Training arguments
        print("Batch size: ", args.train_batch_size)
        training_args = TrainingArguments(
            output_dir=output_dir,
            num_train_epochs=args.num_epochs,
            eval_strategy="steps",
            per_device_train_batch_size=args.train_batch_size,
            per_device_eval_batch_size=args.eval_batch_size,
            warmup_steps=500,
            weight_decay=0.01,
            logging_dir=logs_dir,
            logging_steps=args.num_log_steps,
            eval_steps=args.num_eval_steps,
            fp16=True,
            save_strategy="no"
        )

        # Trainer
        trainer = Trainer(
            model=model,
            args=training_args,
            train_dataset=train_dataset,
            eval_dataset=test_dataset,
            compute_metrics=compute_metrics            
        )

        # Train the model
        trainer.train()
        results = trainer.evaluate()
        print(results)

        i += 1
        # break
