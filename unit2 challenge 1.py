#Define the base class player
class player:     
  def play(selt):
    print("the player is playing cricket.")
#define the derived class batsman
class batsman (player):
  def play (self):
    print("the batsman is batting.")
#define the derived class bowler
class bowler(player):
  def play(selt):
    print("the bowler is bowing.")
#call the objects of batsman and bowler class
batsman=batsman()
bowler=bowler()
#call the play()method for each object
batsman.play()
bowler.play()
