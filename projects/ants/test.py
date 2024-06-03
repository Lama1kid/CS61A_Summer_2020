import importlib

import ants

importlib.reload(ants)
beehive = ants.Hive(ants.AssaultPlan())
dimensions = (2, 9)
gamestate = ants.GameState(None, beehive, ants.ant_types(), ants.dry_layout,
                           dimensions)
ants.bees_win = lambda: None
# QueenAnt Removal
queen = ants.QueenAnt()
impostor = ants.QueenAnt()
place = gamestate.places['tunnel_0_2']
place.add_insect(queen)
breakpoint()
place.remove_insect(queen)
