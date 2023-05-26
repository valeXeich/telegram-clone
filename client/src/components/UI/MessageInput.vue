<template>
    <div class="container">
        <div class="input-block">
        <div class="input-left">
            <label>
                <i class="bi bi-paperclip"></i>
                <input @change="$emit('uploadFile', $event)" type="file" id="file" class="hide-input" name="image">
            </label>
            <input @keyup.enter="addMessage" v-model.trim="message" class="input-message" placeholder="Write a message..." type="text">
        </div>
        <div class="input-right">
            <i class="bi bi-mic"></i>
        </div>
    </div>
    </div>
</template>

<script>
export default {
    props: ['room', 'createMessage'],
    emits: ['uploadFile'],
    data() {
        return {
            message: ''
        }
    },
    methods: {
        addMessage() {
            if (this.message) {
                const message = this.createMessage(this.message, false, null)
                this.$emit('addMessage', 'send', message)
                this.message = ''
            }
        }
    }
}
</script>

<style lang="scss" scoped>

.hide-input {
    display: none;
}

.container {
    min-width: 980px;
    margin: 0 auto;
}

.input-block {
    display: flex;
    width: 922px;
    margin: 15px 0 15px 0;
    padding: 13px;
    background: rgba(255, 255, 255, 0.0512);
    border-radius: 8px;
    align-items: center;
    justify-content: space-between;
    .input-left {
        display: flex;
        align-items: center;
    }
}

.input-message {
    width: 830px;
    color: #fff;
    background: none;
    margin: 0 0 0 20px;
    border: none;
    &::placeholder {
        font-weight: 400;
        font-family: 'Segoe UI Variable';
        line-height: 21px;
        color: #8A8A8A;
    }
}

.bi {
    font-size: 24px;
    color: #8A8A8A;
    cursor: pointer;
}

.bi-paperclip {
 transform: rotate(30deg);
}

</style>