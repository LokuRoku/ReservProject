<template>
    <div>
        <img src="http://ipic.su/img/img7/fs/playbutton.1560260934.png" v-if="!play" @click="VideoShow(true)"></img>
        <iframe v-else width="550" height="320" :src="actualsrc" frameborder="0"></iframe>
    </div>
</template>

<script>
    export default {
        name: "ActualVideo",
        data(){
            return{
                videoid: '',
                timer: '',
                duration: '',
                actualsrc: '',
                play: false,
            }
        },
        created() {
            setInterval(() => {
              this.VideoShow(false);
            }, 4000);

        },
        beforeDestroy(){

        },
        beforeUpdate() {
             // Logs the counter value every second, before the DOM updates.
        },
        methods:{
            VideoShow(actual){
                $.ajax({
                    url: "http://176.99.11.247/api/vi/radio/actualvideo/",
                    type: "GET",
                    success: (response) => {
                        var videosrc = response.data.data[0].video.video;
                        var video = videosrc;
                        var id_video = video.substring(32);
                        var timing = "";
                        var autoplay = "?autoplay=1&amp"
                        if (actual){
                            timing = "?t=" + response.data.data[0].video.time_duration + "&amp;";
                            this.play = true;
                            this.videoid = id_video;
                            this.actualsrc = "http://www.youtube.com/embed/" + id_video + timing + autoplay;
                        }else{
                            if (this.videoid != id_video) {
                                this.videoid = id_video;
                                this.actualsrc = "http://www.youtube.com/embed/" + id_video + timing + autoplay;
                                console.log(this.videosrc);
                            }

                        }

                    },
                    error: (response) => {
                        console.log(response)
                    },
                })
            },
            getTimer(){
                $.ajax({
                    url: "http://176.99.11.247/api/vi/radio/servertime/",
                    type: "GET",
                    success: (response) => {
                        var time_dur = parseInt(response.data, 10);
                        var minutes = (time_dur - time_dur % 60) / 60;
                        var seconds = time_dur - minutes * 60;
                        this.timer = minutes + ":" + seconds;
                    },
                    error: (response) => {
                        console.log(response)
                    },
                })
            },
        }
    }
</script>

<style scoped>

</style>
