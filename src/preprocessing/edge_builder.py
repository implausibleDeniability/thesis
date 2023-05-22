import numpy as np
from tqdm import tqdm

class EdgeBuilder:
    def __init__(self, public_user_id_to_research_id: dict[int, int]):
        self.public_user_id_to_research_id = public_user_id_to_research_id
        
    def build(self, topology: dict) -> np.ndarray:
        edges = []
        for user in tqdm(topology):
            if user['_id'] not in self.public_user_id_to_research_id:
                continue
            user_local_id = self.public_user_id_to_research_id[user['_id']]
            for friend_public_id in user['friends']:
                if friend_public_id not in self.public_user_id_to_research_id:
                    continue
                friend_local_id = self.public_user_id_to_research_id[friend_public_id]
                edges.append((user_local_id, friend_local_id))
        edges = np.array(edges).T
        return edges
