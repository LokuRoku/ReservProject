<template>
    <mu-container class="demo-container is-stripe">
        <mu-row>
            <mu-col span="12"><H1>Для входа в систему введите логин и пароль</H1></mu-col>
        </mu-row>
        <mu-row>
            <mu-col span="12"><input v-model="login" type="text" placeholder="Логин"/></mu-col>
        </mu-row>
        <mu-row>
            <mu-col span="12"><input v-model="password" type="password" placeholder="Пароль"/></mu-col>
        </mu-row>
        <mu-row>
            <mu-col span="12"><button @click="setLogin">Войти</button></mu-col>
        </mu-row>
    </mu-container>
</template>

<script>
    export default {
        name: "Login",
        data(){
            return{
                login: '',
                password: '',
            }
        },
        methods:{
            setLogin(){
                $.ajax({
                    url: "http://127.0.0.1:8000/auth/token/create/",
                    type: "POST",
                    data:{
                        username: this.login,
                        password: this.password,
                    },
                    success: (response) => {
                        alert("Спасибо что зашли!");
                        sessionStorage.setItem("auth_token", response.data.attributes.auth_token);
                        this.$router.push({name: "main"});
                    },
                    error: (response) => {
                        if (response.status === 400){
                            alert("Логин или пароль введены неверно!");
                        }
                    },
                })
            }
        },
    }
</script>

<style scoped>

</style>
