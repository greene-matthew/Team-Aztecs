import javax.swing.JFrame;

public class Main
{
  private static final int X = 900;
  private static final int Y = 568;
  private static Game game = new Game(900, 568);
  
  public Main() {}
  
  public static void main(String[] args) { JFrame frame = new JFrame("Inertia [H4x0R G4M35]");
    frame.setSize(900, 568);
    frame.setDefaultCloseOperation(3);
    frame.add(game);
    frame.setVisible(true);
  }
}