<template>
    <mu-container>
        <mu-row>
            <mu-col span="6">
                <div class="grid-cell">
                    <mu-list>
                        <div v-for="song of songs">
                        <mu-list-item avatar button :ripple="false" >
                            <mu-list-item-content>
                              <mu-list-item-title>{{song.selected_video.name}}</mu-list-item-title>
                              <mu-list-item-sub-title>{{song.selected_video.author}}</mu-list-item-sub-title>
                            </mu-list-item-content>
                            <mu-list-item-action>
                              <mu-list-item-title>{{song.user_choices}}</mu-list-item-title>
                            </mu-list-item-action>
                            <mu-list-item-action>
                              <mu-button icon @click="plusFoSong(song)">+</mu-button>
                            </mu-list-item-action>
                          </mu-list-item>
                          </div>
                      </mu-list>
                  </div>
            </mu-col>
            <mu-col span="6">
                <ActualVideo></ActualVideo>
            </mu-col>
<!--        <div v-for="song of songs">-->
<!--            <table>-->
<!--                <tbody>-->
<!--                    <tr>-->
<!--                        <td>-->
<!--                        </td>-->
<!--                        <td width = "600">-->
<!--                            <span> {{song.selected_video.name}}</span><br>-->
<!--                            <span> {{song.selected_video.author}}</span><br>-->
<!--                        </td>-->
<!--                        <td>{{song.user_choices}}</td>-->
<!--                        <button @click="plusFoSong(song)">+</button>-->
<!--                    </tr>-->
<!--                </tbody>-->
<!--            </table>-->
<!--        </div>-->
            </mu-row>
                <mu-row>

                          <div v-for = "letter of alpabet">
                            <mu-col span="6">
                              <mu-button flat color="primary" @click="getSongs(letter) ">{{letter}}</mu-button>
                            </mu-col>
                          </div>
                </mu-row>
        <mu-row>
          <mu-col>

            <mu-list>
              <div v-for="songletter of songs_list">
                <mu-list-item avatar button :ripple="false" >
                  <mu-list-item-content>
                    <mu-list-item-title>{{songletter.name}}</mu-list-item-title>
                    <mu-list-item-sub-title>{{songletter.author}}</mu-list-item-sub-title>
                  </mu-list-item-content>
                  <mu-list-item-action>
                    <mu-button @click="addSong(songletter)" color="primary">Добавить</mu-button>
                  </mu-list-item-action>
                </mu-list-item>
              </div>
            </mu-list>
            </mu-col>
        </mu-row>
    </mu-container>


</template>

<script>
    import ActualVideo from '@/components/ActualVideo.vue'
    export default {
        name: "SongsMenu",
        components:{
          ActualVideo,
        },
        data(){
            return{
                songs: '',
                tumbnail: '',
                interval: 0,
                letter: '',
                songs_list: '',
                alpabet: '',
            }
        },
        created() {
            this.getAlphabet();
            this.ShowSong();
            $.ajaxSetup({
                headers: {'Authorization': "Token " + sessionStorage.getItem('auth_token')}
            });
            setInterval(() => {
                this.ShowSong();
            }, 5000);

        },
        beforeDestroy(){

        },
        beforeUpdate() {
             // Logs the counter value every second, before the DOM updates.
        },
        methods:{
            ShowSong(){
                $.ajax({
                    url: "http://127.0.0.1:8000/api/vi/radio/songquery/",
                    type: "GET",
                    success: (response) => {
                        this.songs = response.data.data;
                    },
                    error: (response) => {
                        console.log(response)
                    },
                })
            },
            getTumbnail(videosrc){
                video = videosrc;
                id_video = video.substring(32);
                tumbnail = "http://img.youtube.com/vi/" + id_video + "/0.jpg";
                this.tumbnail = tumbnail
            },
            getAlphabet(){
                this.alpabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "0-9"];
            },
            getSongs(letter){
                if (this.letter == letter){
                    this.letter = '';
                    this.songs_list = '';
                } else {
                    $.ajax({
                      url: "http://127.0.0.1:8000/api/vi/radio/songs/?letter=" + letter,
                      type: "GET",
                      success: (response) => {
                        this.songs_list = response.data.data;
                        this.letter = letter;
                      },
                      error: (response) => {
                        this.letter = '';
                        this.songs_list = '';
                        console.log(response)
                      },
                    });
                }
            },
            plusFoSong(song) {
                $.ajax({
                    url: "http://127.0.0.1:8000/api/vi/radio/songquery/",
                    type: "POST",
                    data:{
                        song: song.id,
                    },
                    success: (response) => {
                        this.ShowSong();
                    },
                    error: (response) => {
                        console.log(response);
                    },
                })
            },
            addSong(song) {
                  $.ajax({
                      url: "http://127.0.0.1:8000/api/vi/radio/addsong/",
                      type: "POST",
                      data:{
                          song: song.id,
                      },
                      success: (response) => {
                          this.ShowSong();
                      },
                      error: (response) => {
                          console.log(response);
                      },
                  })
              }
        }

    }
</script>

<style scoped>
    .songs-list {
        margin: 0 3px 0 0;
        box-shadow: 1px 4px 5px #848181;
    }
    .flex-wrapper {
  width: 100%;
  height: 56px;
  margin-top: 8px;
}
.flex-demo {
  width: 200px;
  height: 32px;
  background-color: #e0e0e0;
  text-align: center;
  line-height: 32px;
  margin-left: 8px;
}
.flex-wrapper:first-child {
  margin-top: 0;
}
.flex-demo:first-child {
  margin-left: 0;
}
</style>
