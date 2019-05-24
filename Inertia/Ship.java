import java.awt.Image;
import javax.swing.ImageIcon;








public class Ship
{
  private int x;
  private double dx;
  private int y;
  private double dy;
  private final int MAXDIR = 4;
  

  private final double CH = 1.0D;
  

  private final int MINTEMP = -20;
  
  private int temp;
  
  Image hot;
  
  Image warm;
  
  Image cool;
  Image cold;
  
  public Ship(int i, int j)
  {
    x = i;
    y = j;
    temp = 20;
    dx = 0.0D;
    dy = 0.0D;
    

    hot = new ImageIcon(getClass().getResource("hotship.png")).getImage();
    warm = new ImageIcon(getClass().getResource("warmship.png")).getImage();
    cool = new ImageIcon(getClass().getResource("coolship.png")).getImage();
    cold = new ImageIcon(getClass().getResource("coldship.png")).getImage();
  }
  

  public boolean update(Counter c)
  {
    x = ((int)(x + dx));
    y = ((int)(y + dy));
    if (c.tick())
    {
      temp -= 1;
    }
    
    return temp < -20;
  }
  


  public Image getImage()
  {
    if (temp >= 10)
    {
      return hot;
    }
    if (temp >= 0)
    {
      return warm;
    }
    if (temp >= -10)
    {
      return cool;
    }
    

    return cold;
  }
  


  public void tempCH(int c)
  {
    temp += c;
  }
  


  public void upx()
  {
    if (dx <= 4.0D)
      dx += 1.0D;
  }
  
  public void downx() {
    if (dx >= -4.0D)
      dx -= 1.0D;
  }
  
  public void upy() {
    if (dy >= -4.0D)
      dy -= 1.0D;
  }
  
  public void downy() {
    if (dy <= 4.0D) {
      dy += 1.0D;
    }
  }
  
  public int getX()
  {
    return x;
  }
  
  public int getY() {
    return y;
  }
}