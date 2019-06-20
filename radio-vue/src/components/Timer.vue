<template>
    <div><p>{{timer}}</p></div>
</template>

<script>
    export default {
        name: "Timer",
        data(){
            return{
                interval: 0,
                timer: '',
                seconds: '',
            }
        },
        created() {

            $.ajaxSetup({
                headers: {'Authorization': "Token " + sessionStorage.getItem('auth_token')}
            });
            this.getTimer();
            setInterval(() => {
                this.getTimer();
            }, 4000);
            setInterval(() => {
                this.plusTimer();
            }, 1000);
        },
        methods:{
            getTimer(){
                $.ajax({
                    url: "http://127.0.0.1:8000/api/vi/radio/servertime/",
                    type: "GET",
                    success: (response) => {
                        this.seconds = parseInt(response.data, 10);
                    },
                    error: (response) => {
                        console.log(response)
                    },
                })
            },
            plusTimer(){
                this.seconds = this.seconds - 1;
                if (this.seconds >= 0){
                    var time_dur = parseInt(this.seconds, 10);
                    var minutes = (time_dur - time_dur % 60) / 60;
                    var seconds = time_dur - minutes * 60;
                    var zero = "";
                    if (seconds < 10)
                        zero = "0";
                    this.timer = minutes + ":" + zero + seconds;
                }

            }
        }
    }
</script>

<style scoped>

</style>
