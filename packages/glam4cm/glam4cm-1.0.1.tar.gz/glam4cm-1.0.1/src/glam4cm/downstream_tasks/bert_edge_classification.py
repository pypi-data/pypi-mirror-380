import os
from transformers import TrainingArguments, Trainer
from glam4cm.data_loading.graph_dataset import GraphEdgeDataset
from glam4cm.data_loading.utils import oversample_dataset
from glam4cm.settings import EDGE_CLS_TASK, results_dir
from glam4cm.downstream_tasks.common_args import (
    get_bert_args_parser, 
    get_common_args_parser, 
    get_config_params,
    get_config_str
)
from glam4cm.models.hf import get_model
from glam4cm.downstream_tasks.utils import get_logging_steps
from glam4cm.data_loading.models_dataset import get_models_dataset


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


def get_parser():
    common_parser = get_common_args_parser()
    bert_parser = get_bert_args_parser()
    parser = merge_argument_parsers(common_parser, bert_parser)

    parser.add_argument('--oversampling_ratio', type=float, default=-1)

    return parser


def run(args):
    
    dataset_name = args.dataset
    output_dir = os.path.join(
        results_dir,
        dataset_name,
        f"LM_{EDGE_CLS_TASK}",
        f'{args.edge_cls_label}',
        get_config_str(args)
    )
    if os.path.exists(output_dir):
        print(f"Output directory {output_dir} already exists. Exiting.")
        exit(0)

    config_params = dict(
        include_dummies = args.include_dummies,
        min_enr = args.min_enr,
        min_edges = args.min_edges,
        remove_duplicates = args.remove_duplicates,
        language = args.language,
        reload=args.reload
    )
    
    
    print("Loaded dataset")
    dataset = get_models_dataset(dataset_name, **config_params)

    graph_data_params = get_config_params(args)
    graph_data_params = {**graph_data_params, 'task_type': EDGE_CLS_TASK}

    print("Loading graph dataset")
    graph_dataset = GraphEdgeDataset(dataset, **graph_data_params)
    print("Loaded graph dataset")

    assert hasattr(graph_dataset, f'num_edges_{args.edge_cls_label}'), f"Dataset does not have edge_{args.edge_cls_label} attribute"
    num_labels = getattr(graph_dataset, f"num_edges_{args.edge_cls_label}")


    model_name = args.model_name
    tokenizer = get_tokenizer(model_name, args.use_special_tokens)

    print("Getting Edge Classification data")
    bert_dataset = graph_dataset.get_link_prediction_lm_data(tokenizer=tokenizer)
    
    train_dataset = bert_dataset['train']
    test_dataset = bert_dataset['test']
    set_encoded_labels(train_dataset, test_dataset)


    # exit(0)
    
    if args.oversampling_ratio != -1:
        ind_w_oversamples = oversample_dataset(bert_dataset['train'])
        bert_dataset['train'].inputs = bert_dataset['train'][ind_w_oversamples]

    print("Training model")
    print(f'Number of labels: {num_labels}')
    
    model = get_model(
        args.ckpt if args.ckpt else model_name, 
        num_labels, 
        len(tokenizer), 
        trust_remote_code=args.trust_remote_code
    )

    if args.freeze_pretrained_weights:
        for param in model.base_model.parameters():
            param.requires_grad = False


    logs_dir = os.path.join(
        'logs',
        dataset_name,
        f"LM_{EDGE_CLS_TASK}",
        f'{args.edge_cls_label}',
        f"{graph_dataset.config_hash}",
    )

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
    print(trainer.evaluate())
    trainer.save_model()


if __name__ == '__main__':
    args = get_parser()
    run(args)
