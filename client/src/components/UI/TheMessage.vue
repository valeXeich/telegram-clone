<template>
    <p class="text-message" v-if="!message.is_file">{{ message.content }}</p>
    <div class="file-message" v-else>
        <img :src="message.file" alt="file">
        <p>{{ message.file_type }}</p>
    </div>
</template>

<script>
    export default {
        props: {
            message: {
                type: Object,
                required: true
            }
        }
    }
</script>

<style lang="scss" scoped>
.text-message {
    font-weight: 400;
    font-size: 14px;
    line-height: 19px;
    color: #888888;
}

.file-message {
    display: flex;
    gap: 5px;
    img {
        width: 20px;
        height: 20px;
        border-radius: 2px;
    }
    p {
        font-weight: 400;
        font-size: 14px;
        line-height: 19px;
        color: #0078D4;
    }
}
</style>