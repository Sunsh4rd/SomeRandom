package app;

import music.Music;
import music.MusicPlayer;
import org.springframework.context.support.ClassPathXmlApplicationContext;

public class Main {
    public static void main(String[] args) {
        ClassPathXmlApplicationContext context = new ClassPathXmlApplicationContext(
                "applicationContext.xml"
        );

        MusicPlayer musicPlayer1 = context.getBean("player", MusicPlayer.class);
        MusicPlayer musicPlayer2 = context.getBean("player", MusicPlayer.class);

        for (Music music: musicPlayer1.getPlaylist()) {
            System.out.println(music.getSong());
        }

        for (Music music: musicPlayer2.getPlaylist()) {
            System.out.println(music.getSong());
        }

        System.out.println(musicPlayer1 == musicPlayer2);
        System.out.println(musicPlayer1.equals(musicPlayer2));
        
        context.close();
    }
}