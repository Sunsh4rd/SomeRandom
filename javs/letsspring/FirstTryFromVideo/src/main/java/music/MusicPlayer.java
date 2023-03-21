package music;

import java.util.List;
import java.util.Objects;

public class MusicPlayer {
    private List<Music> playlist;

    public MusicPlayer(List<Music> playlist) {
        this.playlist = playlist;
    }

    public MusicPlayer() {
    }

    public List<Music> getPlaylist() {
        return playlist;
    }

    public void setPlaylist(List<Music> playlist) {
        this.playlist = playlist;
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        MusicPlayer that = (MusicPlayer) o;
        return Objects.equals(playlist, that.playlist);
    }

    @Override
    public int hashCode() {
        return Objects.hash(playlist);
    }
}
