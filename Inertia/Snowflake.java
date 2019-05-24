import java.awt.Image;
import java.util.Random;
import javax.swing.ImageIcon;





public class Snowflake
{
  private boolean benefit;
  private final int BUF = 100;
  

  private int X;
  
  private int Y;
  
  private int there;
  

  public Snowflake(Frame f)
  {
    Random r = new Random();
    X = (r.nextInt(f.getX() - 100) + 50);
    Y = (r.nextInt(f.getY() - 100) + 50);
    
    benefit = (r.nextInt(3) == 0);
    there = (r.nextInt(600) + 200);
  }
  
  public boolean update()
  {
    there -= 1;
    return there > 0;
  }
  
  public Image getImg()
  {
    if (benefit)
    {
      return new ImageIcon(getClass().getResource("redsnowflake.png")).getImage();
    }
    
    return new ImageIcon(getClass().getResource("bluesnowflake.png")).getImage();
  }
  

  public boolean getB()
  {
    return benefit;
  }
  
  public void taken() {
    there = 0;
  }
  

  public int getX()
  {
    return X;
  }
  
  public int getY() {
    return Y;
  }
}