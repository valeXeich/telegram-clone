<template>
    <div class="main">
        <sidebar />
        <TheMain @sendMessage="sendMessage" v-if="room" :room="room" />
    </div>
</template>

<script>
import Sidebar from '@/components/Sidebar.vue';
import TheMain from '@/components/TheMain.vue';

export default {
    components: {
        Sidebar,
        TheMain
    },
    data() {
        return {
            room: null,
            connection: null,
        }
    },
    methods: {
        async getRoom() {
            this.room = await this.$store.dispatch('chat/getRoom', this.$route.params.id);
        },
        sendMessage(action, data) {
            const message = { action, data }
            this.connection.send(JSON.stringify(message))
        }
    },
    async mounted() {
        await this.getRoom();
        const token = this.$store.getters['auth/token']
        this.connection = new WebSocket(`ws://127.0.0.1:8000/chat/ws/${this.$route.params.id}?token=${token}`)
        this.connection.onmessage = event => {
            const message = JSON.parse(event.data)
            if (message.online) {
                this.room.online = message.online
                console.log(message.online)
            } else {
                this.room.messages.push(message)
            }
        }
    },
    beforeUnmount() {
        this.connection.close()
    },
    watch: {
        'room.online'(newValue) {
            if (newValue === 2) {
                const unreadMessages = this.room.messages.filter(msg => !msg.readed)
                unreadMessages.forEach(msg => msg.readed = true)
                if (unreadMessages.length) {
                    const messages = unreadMessages.map(msg => msg.id)
                    this.sendMessage('update', messages)
                }
            }
        }
    }
}
</script>

<style lang="scss" scoped>
.main {
    display: flex;
    width: 100%;
}
</style>