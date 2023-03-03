from playlist import Playlist
from PyQt6.QtCore import QSize
from PyQt6.QtWidgets import (
    QWidget, 
    QMainWindow, 
    QPushButton, 
    QLabel, 
    QVBoxLayout, 
    QHBoxLayout,
    QFileDialog,
    )
from PyQt6.QtMultimedia import QMediaPlayer, QAudioOutput
from PyQt6.QtCore import QUrl


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.UI()
        
    def UI(self):
        
        self.playlist = Playlist()
        
        self.player = QMediaPlayer()
        self.audio = QAudioOutput()
        self.player.setAudioOutput(self.audio)
        self.player.mediaStatusChanged.connect(self.next_song_auto)
        
                
        self.label = QLabel("Add a song to playlist")
        self.label2 = QLabel("Now playing...")
        self.label_song = QLabel("Current song...")
        
        self.prevb = QPushButton("Previous")
        self.prevb.clicked.connect(self.prev_song)
        self.prevb.setEnabled(False)
        
        self.pauseb = QPushButton("Pause")
        self.pauseb.clicked.connect(self.pause)
        self.pauseb.setEnabled(False)
        
        self.playb = QPushButton("Play")
        self.playb.clicked.connect(self.play)
        self.playb.setEnabled(False)
        
        self.nextb = QPushButton("Next")
        self.nextb.clicked.connect(self.next_song)
        self.nextb.setEnabled(False)
        
        self.openb = QPushButton("Add a song")
        self.openb.clicked.connect(self.open_mp3)
        
        hbox = QHBoxLayout()
        hbox.addWidget(self.prevb)
        hbox.addWidget(self.pauseb)
        hbox.addWidget(self.playb)
        hbox.addWidget(self.nextb)
        
        vbox = QVBoxLayout()
        vbox.addWidget(self.label)
        vbox.addWidget(self.openb)
        vbox.addWidget(self.label2)
        vbox.addWidget(self.label_song)
        vbox.addStretch(1)
        vbox.addLayout(hbox)
        
        container = QWidget()
        container.setLayout(vbox)
        self.setCentralWidget(container)
        
        self.setFixedSize(QSize(400, 300)) 
        self.setWindowTitle("Playlist")
        
        self.show()
    
    def open_mp3(self):
        file, _ = QFileDialog.getOpenFileName(self, 'Choose song', './testovoe/songs/', "*.mp3")
        if file != '':
            name = file.split("/")[-1]
            self.playlist.AddSong(name, file)
            if self.playlist.len() == 1:
                self.playb.setEnabled(True)
                self.start()
            if self.playlist.len() == 2:
                self.prevb.setEnabled(True)
                self.nextb.setEnabled(True)
            
    def pause(self):
        self.player.pause()
        
    def start(self):
        self.pauseb.setEnabled(True)
        self.current_song = self.playlist.start_song
        self.label_song.setText(self.current_song.name)
        self.player.setSource(QUrl.fromLocalFile(self.current_song.file))
        self.play()
        
    def next_song_auto(self): 
        #если медиа закончилось, то автоматическое переключение на следующую песню
        if self.player.mediaStatus() == QMediaPlayer.MediaStatus.EndOfMedia:
            self.next_song()
    
    def play(self):
        if self.player.playbackState() != QMediaPlayer.PlaybackState.PlayingState:
            self.player.play()
            
    def prev_song(self):
        file = self.current_song.prev
        if file is not None:
            self.current_song = self.current_song.prev
            self.label_song.setText(self.current_song.name)
            self.player.pause()
            self.player.setSource(QUrl.fromLocalFile(self.current_song.file))
            self.play()
        
        
    def next_song(self):
        file = self.current_song.next
        if file is not None:
            self.current_song = self.current_song.next
            self.label_song.setText(self.current_song.name)
            self.player.pause()
            self.player.setSource(QUrl.fromLocalFile(self.current_song.file))
            self.play()