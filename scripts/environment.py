import gym
from pebsview import readPebsDumpV2

# class PEBSTraceEnv(gym.Env):
#     """PEBS trace based environment.

#     The PEBS trace is assumed to be in a similar format as traces found in the
#     "traces" directory of
#     https://github.com/bgerofi/Heterogeneous-Memory-Management and readable
#     with the method readPebsDumpV2 from the script "pebsview" in the same
#     repository.
#     """

#     def __init__(self, filename):
#         tss, mmaps, munmaps, records, accesses = readPebsDumpV2(filename)
#         self.accesses = accesses
#         self.num_accesses = accesses.shape[0]
#         self.current_access = 0

#     def step(self, action: ActType):
#         reward = 0.0
#         stop = self.current_access >= self.num_access
#         observation = None if stop else self.accesses.iloc[self.current_access, :]
#         debug_info = {}
#         self.current_access += 0 if stop else 1
#         return (observation, reward, stop, debug_info)

#     def reset(self):
#         self.current_access = 1
#         return self.accesses.iloc[0, :]

#     def render(self, mode="human"):
#         raise NotImplementedError
