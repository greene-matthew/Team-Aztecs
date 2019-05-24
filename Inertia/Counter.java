


public class Counter
{
  private int pregame;
  private int tickShip;
  
  public Counter()
  {
    pregame = 1000;
    tickShip = 25;
  }
  

  public boolean update()
  {
    if (pregame > 0)
    {
      pregame -= 1;
    }
    return pregame <= 0;
  }
  

  public boolean tick()
  {
    tickShip -= 1;
    if (tickShip <= 0)
    {
      tickShip = 25;
      return true;
    }
    return false;
  }
}