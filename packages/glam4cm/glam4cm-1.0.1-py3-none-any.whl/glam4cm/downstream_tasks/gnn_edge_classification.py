import os
from glam4cm.data_loading.graph_dataset import GraphEdgeDataset
from glam4cm.models.gnn_layers import GNNConv, EdgeClassifer
from glam4cm.settings import EDGE_CLS_TASK
from glam4cm.data_loading.models_dataset import get_models_dataset
from glam4cm.tokenization.special_tokens import *
from glam4cm.trainers.gnn_edge_classifier import GNNEdgeClassificationTrainer as Trainer
from glam4cm.utils import merge_argument_parsers, set_torch_encoding_labels
from glam4cm.downstream_tasks.common_args import (
    get_common_args_parser, 
    get_config_params, 
    get_gnn_args_parser
)


def get_parser():
    common_parser = get_common_args_parser()
    gnn_parser = get_gnn_args_parser()
    parser = merge_argument_parsers(common_parser, gnn_parser)
    return parser


def run(args):

    
    
    config_params = dict(
        include_dummies = args.include_dummies,
        min_enr = args.min_enr,
        min_edges = args.min_edges,
        remove_duplicates = args.remove_duplicates,
        reload = args.reload,
        language = args.language
    )
    dataset_name = args.dataset

    dataset = get_models_dataset(dataset_name, **config_params)

    graph_data_params = get_config_params(args)
    graph_data_params = {**graph_data_params, 'task_type': EDGE_CLS_TASK}
    print("Using model: ", graph_data_params['embed_model_name'])
    if args.ckpt:
        print("Using checkpoint: ", args.ckpt)
        
    # if args.use_embeddings:
    #     graph_data_params['embed_model_name'] = os.path.join(results_dir, dataset_name, f'{args.edge_cls_label}')

    print("Loading graph dataset")
    graph_dataset = GraphEdgeDataset(dataset, **graph_data_params)
    print("Loaded graph dataset")

    graph_torch_data = graph_dataset.get_torch_dataset()
    exclude_labels = getattr(graph_dataset, f"edge_exclude_{args.edge_cls_label}")
    set_torch_encoding_labels(graph_torch_data, f"edge_{args.edge_cls_label}", exclude_labels)

    input_dim = graph_torch_data[0].x.shape[1]

    model_name = args.gnn_conv_model
    hidden_dim = args.hidden_dim
    output_dim = args.output_dim
    num_conv_layers = args.num_conv_layers
    num_mlp_layers = args.num_mlp_layers
    num_heads = args.num_heads
    residual = False
    l_norm = args.l_norm
    dropout = args.dropout
    aggregation = args.aggregation

    num_edges_label = f"num_edges_{args.edge_cls_label}"
    assert hasattr(graph_dataset, num_edges_label), f"Graph dataset does not have attribute {num_edges_label}"
    num_classes = getattr(graph_dataset, num_edges_label)

    edge_dim = graph_dataset[0].data.edge_attr.shape[1] if args.use_edge_attrs else None

    ue = "" if not args.use_edge_attrs else "_ue"
    
    logs_dir = os.path.join(
        "logs",
        dataset_name,
        f"GNN_{EDGE_CLS_TASK}",
        f"{args.edge_cls_label}{ue}",
        f"{graph_dataset.config_hash}",
    )
    

    gnn_conv_model = GNNConv(
        model_name=model_name,
        input_dim=input_dim,
        hidden_dim=hidden_dim,
        out_dim=output_dim,
        num_layers=num_conv_layers,
        num_heads=num_heads,
        residual=residual,
        l_norm=l_norm,
        dropout=dropout,
        aggregation=aggregation,
        edge_dim=edge_dim
    )

    clf_input_dim = output_dim*num_heads if args.num_heads else output_dim
    mlp_predictor = EdgeClassifer(
        input_dim=clf_input_dim,
        hidden_dim=hidden_dim,
        num_layers=num_mlp_layers, 
        num_classes=num_classes,
        edge_dim=edge_dim,
        bias=args.bias,
    )

    trainer = Trainer(
        gnn_conv_model, 
        mlp_predictor, 
        graph_torch_data,
        cls_label=args.edge_cls_label,
        lr=args.lr,
        num_epochs=args.num_epochs,
        batch_size=args.batch_size,
        use_edge_attrs=args.use_edge_attrs,
        logs_dir=logs_dir,
    )

    print("Training GNN Edge Classification model")
    trainer.run()
