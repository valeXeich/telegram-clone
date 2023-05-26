<template>
    <div class="main">
        <TheHeader :user="room.user" />
        <div class="content" id="content">
            <div class="container-test">
                <ChatMessage :messages="room.messages" />
            </div>
        </div>

        <MessageInput :createMessage="createMessage" @uploadFile="uploadFile" @addMessage="addMessage" />

        <Teleport to="body">
            <FileModal v-if="modal" :createMessage="createMessage" title="Send Photo" :previewFile="previewFile"
                @close="closeModal" @addMessage="addMessage" />
        </Teleport>
    </div>
</template>

<script>
import MessageInput from './UI/MessageInput.vue';
import TheHeader from './TheHeader.vue'
import FileModal from './UI/FileModal/FileModal.vue'
import ChatMessage from './UI/ChatMessage/ChatMessage.vue';
import { getCurrentTime } from "@/utils/currentTime";

export default {
    props: {
        room: Object
    },
    components: {
        MessageInput,
        TheHeader,
        FileModal,
        ChatMessage
    },
    data() {
        return {
            modal: false,
            previewFile: {},
        }
    },
    methods: {
        uploadFile(event) {
            const file = event.target.files[0];
            console.log(file)
            let url = null;
            if (file.type.includes('video') || file.type.includes('image')) {
                url = URL.createObjectURL(file);
            }
            this.previewFile = { name: file.name, type: file.type, url, size: file.size, file }
            this.modal = true;
            event.target.value = ''
        },
        closeModal() {
            this.modal = false;
            this.file = {};
        },
        addMessage(action, message) {
            this.modal = false;
            this.$emit('sendMessage', action, message)
        },
        createMessage(content, isFile, fileType, encodedData = null) {
            const createdAt = getCurrentTime();
            const user = this.$store.getters['user/user']
            const message = {
                content: content,
                is_file: isFile,
                readed: this.room.online === 2 ? true : false,
                created_at: createdAt,
                user: user
            };
            if (isFile) {
                message.file = this.previewFile.url;
                message.file_name = this.previewFile.name;
                message.size = this.previewFile.size;
                message.file_type = fileType;
                message.encodedData = encodedData;
            }
            return message;
        },
    },
    mounted() {
        const scroll = document.getElementById("content");
        scroll.scrollTop = scroll.scrollHeight;
    }
}
</script>

<style lang="scss" scoped>
.container-test {
    max-width: 980px;
    margin: 0 auto;
}

.main {
    background-image: url(https://web.telegram.org/a/chat-bg-pattern-dark.ad38368a9e8140d0ac7d.png);
    background-color: black;
    width: 100%;
    display: flex;
    flex-direction: column;
    height: 100vh;
}

.content {
    flex: 1;
    overflow-y: auto;
    height: 100vh;

    &::-webkit-scrollbar {
        width: 5px;
    }

    &::-webkit-scrollbar-track {
        background: transparent;
    }

    &::-webkit-scrollbar-thumb {
        background: rgba(#979A9F, 0.2);
        border-radius: 9999px;
    }

    &::-webkit-scrollbar-thumb:hover {
        background: rgba(#555, 0.2);
    }
}
</style>