<template>
    <div class="background">
        <div class="container">
            <p class="title">Sign in</p>
            <AlertError v-if="error" :error="error"/>
            <form class="form-control" @submit.prevent="login">
                <InputForm v-model="username" type="text" placeholder="Username"/>
                <InputForm v-model="password" type="password" placeholder="Password"/>
                <button class="form-btn">Sign In</button>
            </form>
            <router-link to="/signup" class="btn">Sign Up</router-link>
        </div>
    </div>
</template>

<script>
import InputForm from '@/components/UI/InputForm.vue'
import AlertError from '@/components/UI/AlertError.vue'

export default {
    components: {
        InputForm, AlertError
    },
    data() {
        return {
            username: '',
            password: '',
            error: ''
        }
    },
    methods: {
        async login() {
            try {
                await this.$store.dispatch('auth/login', {
                    username: this.username,
                    password: this.password
                })
                this.$router.push('/')
            } catch (e) {
                this.error = e.message
            }
        }
    }
}
</script>

<style lang="scss" scoped>

.background {
    background-color: #212121;
    height: 100vh;
}

.title {
    font-size: 32px;
    color: $white;
    font-weight: 500;
}

.container {
    text-align: center;
    margin: 0 auto;
    height: 100%;
    max-width: 360px;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
}

.form-control {
    display: flex;
    flex-direction: column;
    padding: 10px;
    width: 100%;
    gap: 10px;
}

.form-btn {
    background-color: #8774e1;
    border: none;
    color: $white;
    text-transform: uppercase;
    font-weight: 600;
    height: 3rem;
    font-family: "Segoe UI Variable";
    padding: 0 1rem;
    transition: background-color .15s, color .15s;
    border-radius: 0.625rem;
    cursor: pointer;
    &:hover {
      background-color: #7b71c6;
    }
}

.btn {
    width: 100%;
    text-transform: uppercase;
    border: none;
    color: #8774e1;
    background-color: transparent;
    height: 3rem;
    font-family: "Segoe UI Variable";
    display: flex;
    justify-content: center;
    align-items: center;
    transition: background-color .15s, color .15s;
    border-radius: 0.625rem;
    &:hover {
        background-color: #292730;
    }
}

</style>