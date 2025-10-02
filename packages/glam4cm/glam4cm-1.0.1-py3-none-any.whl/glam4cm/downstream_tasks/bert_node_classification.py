import numpy as np
from glam4cm.models.hf import get_model
from glam4cm.downstream_tasks.common_args import (
    get_bert_args_parser, 
    get_common_args_parser, 
    get_config_params,
    get_config_str
)
import os
from transformers import TrainingArguments, Trainer
from glam4cm.data_loading.graph_dataset import GraphNodeDataset
from glam4cm.data_loading.utils import oversample_dataset
from glam4cm.downstream_tasks.utils import get_logging_steps
from glam4cm.data_loading.models_dataset import get_models_dataset
from glam4cm.settings import NODE_CLS_TASK, results_dir
from glam4cm.tokenization.special_tokens import *
from sklearn.model_selection import StratifiedKFold

from sklearn.metrics import (
    accuracy_score, 
    f1_score, 
    recall_score,
    balanced_accuracy_score
)

from glam4cm.tokenization.utils import get_tokenizer
from glam4cm.utils import merge_argument_parsers, set_encoded_labels, set_seed



def compute_metrics(pred):
    labels = pred.label_ids
    preds = pred.predictions.argmax(-1)
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


def get_num_labels(dataset):
    train_labels = dataset['train'][:]['labels'].unique().tolist()
    test_labels = dataset['test'][:]['labels'].unique().tolist()
    return len(set(train_labels + test_labels))


def get_parser():
    common_parser = get_common_args_parser()
    bert_parser = get_bert_args_parser()
    parser = merge_argument_parsers(common_parser, bert_parser)

    parser.add_argument('--oversampling_ratio', type=float, default=-1)

    return parser


def run(args):
    
    dataset_name = args.dataset
    print("Training model")
    output_dir = os.path.join(
        results_dir,
        dataset_name,
        f'LM_{NODE_CLS_TASK}',
        f'{args.node_cls_label}',
        get_config_str(args)
    )

    # if os.path.exists(output_dir):
    #     print(f"Output directory {output_dir} already exists. Exiting.")
    #     exit(0)

    config_params = dict(
        include_dummies = args.include_dummies,
        min_enr = args.min_enr,
        min_edges = args.min_edges,
        remove_duplicates = args.remove_duplicates,
        reload=args.reload,
        language = args.language
    )
    dataset_name = args.dataset
    distance = args.distance
    dataset = get_models_dataset(dataset_name, **config_params)

    print("Loaded dataset")

    graph_data_params = {**get_config_params(args), 'task_type': NODE_CLS_TASK}
    print("Loading graph dataset")
    
    k = int(1 / args.test_ratio)
    
    for i in range(k):
        set_seed(np.random.randint(0, 1000))
        graph_dataset = GraphNodeDataset(dataset, **graph_data_params)
        print("Loaded graph dataset")

        assert hasattr(graph_dataset, f'num_nodes_{args.node_cls_label}'), f"Dataset does not have node_{args.node_cls_label} attribute"
        num_labels = getattr(graph_dataset, f"num_nodes_{args.node_cls_label}")

        model_name = args.model_name
        tokenizer = get_tokenizer(model_name, use_special_tokens=args.use_special_tokens)

        print("Getting node classification data")
        bert_dataset = graph_dataset.get_node_classification_lm_data(
            label=args.node_cls_label,
            tokenizer=tokenizer,
            distance=distance,
        )

        # exit(0)

        if args.oversampling_ratio != -1:
            ind_w_oversamples = oversample_dataset(bert_dataset['train'])
            bert_dataset['train'].inputs = bert_dataset['train'][ind_w_oversamples]
        
        
        model = get_model(
            args.ckpt if args.ckpt else model_name, 
            num_labels=num_labels, 
            len_tokenizer=len(tokenizer), 
            trust_remote_code=args.trust_remote_code
        )

        if args.freeze_pretrained_weights:
            for param in model.base_model.parameters():
                param.requires_grad = False


        logs_dir = os.path.join(
            'logs',
            dataset_name,
            f'BERT_{NODE_CLS_TASK}',
            f'{args.node_cls_label}',
            f"{graph_dataset.config_hash}_{i}",
        )

        print("Output Dir: ", output_dir)
        print("Logs Dir: ", logs_dir)
        print("Len Train Dataset: ", len(bert_dataset['train']))
        print("Len Test Dataset: ", len(bert_dataset['test']))
        
        train_dataset = bert_dataset['train']
        test_dataset = bert_dataset['test']
        set_encoded_labels(train_dataset, test_dataset)

        
        print("Num epochs: ", args.num_epochs)
        
        logging_steps = get_logging_steps(
            len(train_dataset), 
            args.num_epochs, 
            args.train_batch_size
        )

        training_args = TrainingArguments(
            output_dir=output_dir,
            num_train_epochs=args.num_epochs,
            per_device_train_batch_size=args.train_batch_size,
            per_device_eval_batch_size=args.eval_batch_size,
            weight_decay=0.01,
            logging_dir=logs_dir,
            logging_steps=logging_steps,
            eval_strategy='steps',
            eval_steps=logging_steps,
            # save_steps=args.num_save_steps,
            # save_total_limit=2,
            # load_best_model_at_end=True,
            fp16=True,
            save_strategy="no"
        )

        trainer = Trainer(
            model=model,
            args=training_args,
            train_dataset=bert_dataset['train'],
            eval_dataset=bert_dataset['test'],
            compute_metrics=compute_metrics
        )

        trainer.train()
        results = trainer.evaluate()
        
        # with open(os.path.join(output_dir, 'results.txt'), 'a') as f:
        #     f.write(str(results))
        #     f.write('\n')
        
        print(results)

        trainer.save_model()
        break


if __name__ == '__main__':
    args = get_parser()
    run(args)
