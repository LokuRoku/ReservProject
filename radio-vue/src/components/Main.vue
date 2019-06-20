<template>
    <mu-container>
        <mu-appbar style="width: 100%;" color="primary">
            Радиобудка
            <Timer flat slot="right" v-if="auth"></Timer>
            <mu-button flat slot="right" v-if="auth" @click="exit">Выход</mu-button>
            <mu-button flat slot="right" v-else @click="goLogin">Вход</mu-button>
            <mu-button flat slot="right" v-if="!auth" @click="goRegistration">Регистрация</mu-button>

        </mu-appbar>

        <mu-row>
            <SongsMenu v-if="auth"></SongsMenu>


        </mu-row>
    </mu-container>
</template>

<script>
    import SongsMenu from '@/components/SongsMenu.vue'
    import Timer from '@/components/Timer.vue'
    import ActualVideo from '@/components/ActualVideo.vue'

    export default {
        name: "Main",
        components: {
            SongsMenu,
            Timer,
            ActualVideo
        },
        computed:{
            auth(){
                if(sessionStorage.getItem('auth_token')) {
                    return true
                }
            },
        },
        methods: {
            goLogin(){
                this.$router.push({name: "login"})
            },
            goRegistration(){
                this.$router.push({name: "registration"})
            },
            exit(){
                sessionStorage.removeItem('auth_token');
                window.location = '/'
            }
        },
    }
</script>

<style scoped>

</style>
