import java.io.PrintStream;
import javax.sound.sampled.AudioSystem;
import javax.sound.sampled.Clip;





public class AudioPlayer
{
  private static boolean play;
  private static boolean debug;
  private static Thread musicPlayer;
  private static AudioPlayer audioPlayer;
  
  public AudioPlayer()
  {
    debug = true;
    play = false;
  }
  
  public AudioPlayer(boolean d, boolean p)
  {
    debug = d;
    play = p;
  }
  




  public void miniClip(String filename)
  {
    try
    {
      Clip clip = AudioSystem.getClip();
      clip.open(AudioSystem.getAudioInputStream(getClass()
        .getResource(filename)));
      clip.start();
    }
    catch (Exception e) {
      if (debug) {
        System.out.println(e);
      }
    }
  }
  



  public void handleAudio(String filename)
  {
    String FILENAME = filename;
    musicPlayer = new AudioPlayer.1(this, FILENAME);
    








































    musicPlayer.start();
  }
  
  public void setDebug(boolean d)
  {
    debug = d;
  }
  
  public void setContinue(boolean p)
  {
    play = p;
  }
}