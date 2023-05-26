<template>
    <div class="header">
        <div class="container">
            <div class="chat-info">
                <img class="avatar" :src="`${user.avatar}.png`" alt="avatar">
                <div class="user-info">
                    <p class="user-username">{{ user.username }}</p>
                    <p class="user-status">online</p>
                </div>
            </div>
            <div class="actions">
                <i class="bi bi-search"></i>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    props: {
        user: {
            type: Object,
            required: true
        }
    }
}
</script>

<style lang="scss" scoped>

.header {
    min-height: 60px;
    width: 100%;
    background-color: rgb(33,33,33);
}

.container {
    max-width: 924px;
    height: 100%;
    margin: 0 auto;
    display: flex;
    justify-content: space-between;
    align-items: center;
}

.chat-info {
    display: flex;
    align-items: center;
    gap: 10px;
    .user-info {
        .user-username {
            font-weight: 600;
            line-height: 21px;
            color: #FFFFFF;
        }
        .user-status {
            font-size: 12px;
            line-height: 16px;
            color: #0F80D7;
        }
    }
}

.actions {
        color: #fff;
        font-size: 20px;
    }
</style>