import pytest
from snake_game import game

def test_game_start():
    # Apenas verifica se a função main() existe no jogo
    assert hasattr(game, "main")
