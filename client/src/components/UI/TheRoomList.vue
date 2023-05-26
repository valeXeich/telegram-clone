<template>
    <router-link v-for="room in rooms" :key="room.id" :to="`/room/${room.id}`">
        <div class="card">
        <div class="container">
            <div class="card-left">
            <img :src="`${room.user.avatar}.png`" alt="avatar" class="avatar">
            <div class="card-info">
                <p class="info-username">{{ room.user.username }}</p>
                <the-message :message="room.message"/>
            </div>
            </div>
            <div class="card-right">
                <p class="card-time">{{ room.message.created_at }}</p>
                <div class="card-unread" v-if="room.total_unread">
                    {{ room.total_unread }}
                </div>
            </div>
        </div>
        </div>
    </router-link>
</template>

<script>
import TheMessage from './TheMessage.vue';
import { mapGetters } from 'vuex';

export default { 
    components: {
        TheMessage
    },
    computed: {
        ...mapGetters({
            rooms: 'chat/rooms'
        })
    },
    async mounted() {
        await this.$store.dispatch('chat/getRooms');
    }
}
</script>


<style lang="scss" scoped>

.container {
    max-width: 391px;
    margin: 0 auto;
    display: flex;
    justify-content: space-between;
    padding: 12.5px 0;
}


.card {
    cursor: pointer;
    &:hover {
        background: rgba(255, 255, 255, 0.0605);
        border-radius: 4px;
    }
}

.card-active {
    cursor: pointer;
    background: rgba(218, 209, 209, 0.164);
    border-radius: 4px;
}



.card-right {
    display: flex;
    flex-direction: column;
    align-items: flex-end;
    gap: 5px;
    .card-time {
        font-weight: 400;
        font-size: 14px;
        line-height: 19px;
        color: #838383;
    }

    .card-unread {
        width: 25px;
        height: 18px;
        padding: 2px;
        background: #0078D4;
        border-radius: 20px;
        display: flex;
        justify-content: center;
        align-items: center;
        font-size: 14px;
    }
}

.card-left {
    display: flex;
    gap: 10px;
    .card-info {
        align-self: center;
        .info-username {
            margin: 0 0 5px 0;
            font-weight: 600;
            line-height: 21px;
        }
    }
}

</style>