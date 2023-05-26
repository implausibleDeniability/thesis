import torch
from torch.nn import ReLU, Dropout, Embedding
from torch_geometric.nn import MLP, Sequential, BatchNorm
from torch_geometric.nn.conv import GCNConv, ResGatedGraphConv, GATConv, GINConv

class NN(torch.nn.Module):
    def __init__(
        self,
        input_dim: int,
        hidden_dim: int,
        output_dim: int,
        graph_conv: ConvType,
        depth: int,
        mlp_depth: int,
        embeddings: list[int],
        use_batchnorm: bool=False,
        dropout: float=0,
    ):
        super().__init__()
        self.hidden_dim = hidden_dim
        self.embedding_dims = [4, 4, 2, 4, 4, 4, 4]
        self.use_batchnorm = False
        self.dropout = dropout
        self.input_mlp = MLP([input_dim + sum(self.embedding_dims)] + [hidden_dim] * mlp_depth, plain_last=False)
        self.conv_layers = Sequential(
            "x, edge_index",
            [
                self._build_conv_layer(graph_conv)
                for _ in range(depth)
            ]
        )
        self.output_mlp = MLP([hidden_dim] * mlp_depth + [output_dim])
        self.sigmoid = torch.nn.Sigmoid()
        self._build_embeddings(embeddings)
        
    def _build_conv_layer(self, conv_type: ConvType):
        if conv_type == ConvType.gcn:
            conv = (
                GCNConv(self.hidden_dim, self.hidden_dim),
                'x, edge_index -> x',
            )
        elif conv_type == ConvType.gat:
            conv = (
                GATConv(self.hidden_dim, self.hidden_dim),
                'x, edge_index -> x',
            )
        elif conv_type == ConvType.res:
            conv = (
                ResGatedGraphConv(self.hidden_dim, self.hidden_dim),
                'x, edge_index -> x',
            )
        elif conv_type == ConvType.gin:
            conv = (
                GINConv(MLP([self.hidden_dim, self.hidden_dim], train_eps=True)),
                'x, edge_index -> x',
            )
        else:
            raise NotImplementedError()
        conv_layer = [conv]
        if self.use_batchnorm:
            conv_layer.append((BatchNorm(self.hidden_dim), 'x -> x'))
        conv_layer.append(ReLU(inplace=True))
        if self.dropout is not None:
            conv_layer.append((Dropout(p=self.dropout), 'x -> x'))
        conv_layer = Sequential("x, edge_index", conv_layer)
        return conv
    
    def _build_embeddings(self, embedding_sizes):
        self.city_embedding = Embedding(embedding_sizes[0], embedding_dim=self.embedding_dims[0], scale_grad_by_freq=True)
        self.country_embedding = Embedding(embedding_sizes[1], embedding_dim=self.embedding_dims[1], scale_grad_by_freq=True)
        self.sex_embedding = Embedding(embedding_sizes[2], embedding_dim=self.embedding_dims[2], scale_grad_by_freq=True)
        self.politics_embedding = Embedding(embedding_sizes[3], embedding_dim=self.embedding_dims[3], scale_grad_by_freq=True)
        self.life_embedding = Embedding(embedding_sizes[4], embedding_dim=self.embedding_dims[4], scale_grad_by_freq=True)
        self.people_embedding = Embedding(embedding_sizes[5], embedding_dim=self.embedding_dims[5], scale_grad_by_freq=True)
        self.alcohol_embedding = Embedding(embedding_sizes[6], embedding_dim=self.embedding_dims[6], scale_grad_by_freq=True)
        self.embeddings = [
            self.city_embedding,
            self.country_embedding,
            self.sex_embedding,
            self.politics_embedding,
            self.life_embedding,
            self.people_embedding,
            self.alcohol_embedding,
        ]
    
    def forward(self, features, edge_index):
        numerical_features = torch.Tensor(features.numerical)
        categorical_embeddings = self._extract_embeddings(torch.tensor(features.categorical, dtype=torch.long))
        x = torch.cat([numerical_features, categorical_embeddings], dim=-1)
        x = self.input_mlp(x)
        x = self.conv_layers(x, edge_index)
        x = self.output_mlp(x)
        probs = self.sigmoid(x)
        return probs
    
    def _extract_embeddings(self, categorical_features) -> torch.Tensor:
        feature_embeds = []
        for feature_idx in range(categorical_features.shape[1]):
            feature = categorical_features[:, feature_idx]
            feature_embed = self.embeddings[feature_idx](feature)
            feature_embeds.append(feature_embed)
        feature_embeds = torch.cat(feature_embeds, dim=-1)
        return feature_embeds
