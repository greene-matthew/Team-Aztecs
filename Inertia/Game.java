import java.awt.Color;
import java.awt.Graphics;
import java.awt.Graphics2D;
import java.awt.Image;
import java.awt.Rectangle;
import java.util.ArrayList;
import javax.swing.ImageIcon;
import javax.swing.JPanel;
import javax.swing.Timer;























public class Game
  extends JPanel
{
  private int timeout;
  private Frame frame;
  private Timer timer;
  private Counter counter;
  private AudioPlayer audio;
  private Ship ship;
  private Image background;
  private int time;
  boolean running;
  boolean paused;
  boolean end;
  boolean winner;
  ArrayList<Snowflake> snowflakes;
  
  public Game(int x, int y)
  {
    addKeyListener(new Game.TAdapter(this, null));
    setFocusable(true);
    
    timeout = 100;
    
    frame = new Frame(x, y);
    counter = new Counter();
    background = new ImageIcon(getClass().getResource("Ice.jpg")).getImage();
    ship = new Ship(frame.getX() / 2, frame.getY() / 2);
    
    running = false;
    paused = false;
    end = false;
    winner = false;
    
    audio = new AudioPlayer();
    audio.setDebug(false);
    audio.handleAudio("opening.wav");
    audio.setContinue(true);
    
    snowflakes = new ArrayList();
    
    for (int i = 0; i < 12; i++)
    {
      snowflakes.add(new Snowflake(frame));
    }
    
    time = 10;
    timer = new Timer(time, new Game.Listener(this, null));
    timer.start();
  }
  
  public void paintComponent(Graphics g)
  {
    Graphics2D g2d = (Graphics2D)g;
    

    g2d.drawImage(background, 0, 0, null);
    g2d.setColor(Color.WHITE);
    
    if (!running)
    {
      g2d.drawString("INERTIA!!!", frame.getX() / 4, frame.getY() / 5 - 80);
      g2d.drawString("In this frozen world, you must fight for survival.", frame.getX() / 4, frame.getY() / 5 - 60);
      g2d.drawString("The red snowflakes have the power to heat your ship, but the blue ones will cool it down.", frame.getX() / 4, frame.getY() / 5 - 40);
      g2d.drawString("Your ship will slowly cool over time, and, if it gets too cold, you will die", frame.getX() / 4, frame.getY() / 5 - 20);
      g2d.drawString("Don't touch the edges, or you will freeze instantaneously!", frame.getX() / 4, frame.getY() / 5);
      g2d.drawString("Survive for two minutes to be victorius! Good Luck!", frame.getX() / 4, frame.getY() / 5 + 20);
    }
    else if ((running) && (!end) && (!winner))
    {
      g2d.drawImage(ship.getImage(), ship.getX(), ship.getY(), null);
      for (Snowflake s : snowflakes)
      {
        g2d.drawImage(s.getImg(), s.getX(), s.getY(), null);
      }
    }
    else if (end)
    {
      g2d.drawString("GAME OVER", frame.getX() / 4, frame.getY() / 5 - 40);
      g2d.drawString("You froze to death :(", frame.getX() / 4, frame.getY() / 5 - 20);
      g2d.drawString("Press ENTER to try again.", frame.getX() / 4, frame.getY() / 5);
    }
    else if (winner)
    {
      g2d.drawString("GAME OVER", frame.getX() / 4, frame.getY() / 5 - 40);
      g2d.drawString("You survived against all odds!", frame.getX() / 4, frame.getY() / 5 - 20);
      g2d.drawString("Press ENTER to play again.", frame.getX() / 4, frame.getY() / 5);
    }
  }
  
  public void update()
  {
    if (!running)
    {
      running = counter.update();
      if (running)
      {
        audio.setContinue(false);
        try
        {
          Thread.sleep(2000L);
        }
        catch (InterruptedException localInterruptedException) {}
        

        audio.handleAudio("maingame.wav");
        audio.setContinue(true);
      }
    }
    

    if (running)
    {
      if (end)
      {
        timer.stop();
        audio.setContinue(false);
        try
        {
          Thread.sleep(2000L);
        }
        catch (InterruptedException localInterruptedException1) {}
      }
      


      if (winner)
      {
        timer.stop();
        audio.setContinue(false);
        try
        {
          Thread.sleep(2000L);
        }
        catch (InterruptedException localInterruptedException2) {}
      }
      
      boolean t;
      
      for (int i = 0; i < 12; i++)
      {
        t = ((Snowflake)snowflakes.get(i)).update();
        if (!t)
        {
          snowflakes.remove(i);
          snowflakes.add(new Snowflake(frame));
        }
      }
      end = ship.update(counter);
      

      for (Snowflake s : snowflakes)
      {
        Rectangle r = new Rectangle(s.getX(), s.getY(), s.getImg().getWidth(null), s.getImg().getHeight(null));
        if (r.intersects(new Rectangle(ship.getX(), ship.getY(), ship.getImage().getWidth(null), ship.getImage().getHeight(null))))
        {
          if (s.getB())
          {
            ship.tempCH(5);
          }
          else
          {
            ship.tempCH(-5);
          }
          s.taken();
        }
      }
      

      if ((ship.getX() <= 0) || (ship.getX() + ship.getImage().getWidth(null) >= frame.getX()) || (ship.getY() <= 0) || (ship.getY() + ship.getImage().getHeight(null) >= frame.getY() - 20))
      {
        end = true;
      }
      

      timeout -= 1;
      if (timeout <= 0)
      {
        winner = true;
      }
    }
  }
}