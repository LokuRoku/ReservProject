<template>
    <mu-container class="demo-container is-stripe">
        <mu-row>
            <mu-col span="12"><H3>Для того чтобы зарегистрироваться</H3><br>
            <H3>введите логин и пароль,</H3><br>
            <H3>затем нажмите Зарегистрироваться</H3><br></mu-col>
        </mu-row>
        <mu-row>
            <mu-col span="12"><input v-model="login" type="text" placeholder="Имя пользователя"/></mu-col>
        </mu-row>
        <mu-row>
            <mu-col span="12"><input v-model="password" type="password" placeholder="Пароль"/></mu-col>
        </mu-row>
        <mu-row>
            <mu-col span="12"><button @click="setLogin">Зарегистрироваться</button></mu-col>
        </mu-row>
    </mu-container>
</template>

<script>
    export default {
        name: "Registration",
        data(){
            return{
                login: '',
                password: '',
            }
        },
        methods:{
            setLogin(){
                $.ajax({
                    url: "http://127.0.0.1:8000/api/vi/radio/createuser/",
                    type: "POST",
                    data:{
                        username: this.login,
                        password: this.password,
                    },
                    success: (response) => {
                        alert("Регистрация произведена успешно!");
                        this.$router.push({name: "login"});
                    },
                    error: (response) => {
                        if (response.status === 400){
                            alert("Произошла ошибка!");
                        }
                    },
                })
            }
        },
    }
</script>

<style scoped>

</style>
