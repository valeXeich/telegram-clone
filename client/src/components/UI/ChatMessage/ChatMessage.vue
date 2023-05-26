<template>
  <div :class="messageClasses(message)" v-for="message in messages" :key="message.id">
    <img class="avatar" :src="`${message.user.avatar}.png`" alt="avatar" />
    <component :is="getComponentName(message)" :message="message" @click="mediaView(message)" />
  </div>
  <Teleport to="body">
    <ModalMediaPreview v-if="modal" :media="media" @close="modal = false" />
  </Teleport>
</template>

<script>
import ChatTextMessage from "./ChatTextMessage.vue";
import ChatImageMessage from "./ChatImageMessage.vue";
import ChatVideoMessage from "./ChatVideoMessage.vue";
import ChatDocumentMessage from "./ChatDocumentMessage.vue";
import ModalMediaPreview from "../ModalMediaPreview.vue";
import { mapGetters } from "vuex";

export default {
  components: {
    ChatTextMessage,
    ChatImageMessage,
    ChatVideoMessage,
    ChatDocumentMessage,
    ChatTextMessage,
    ModalMediaPreview
  },
  props: {
    messages: Array,
  },
  data() {
    return {
      modal: false,
      media: null
    }
  },
  computed: {
    ...mapGetters({
      user: 'user/user'
    })
  },
  methods: {
    mediaView(message) {
      const isImage = this.isPicture(message)
      if (isImage || this.isVideo(message)) {
        this.media = {
          url: message.file,
          isImage
        }
        this.modal = true;
      }
    },
    isPicture(message) {
      return message.file_type === "Picture"
    },
    isVideo(message) {
      return message.file_type === "Video"
    },
    isDocument(message) {
      return message.file_type === "Document"
    },
    getComponentName(message) {
      if (!message.is_file) {
        return 'ChatTextMessage';
      } else if (this.isPicture(message)) {
        return 'ChatImageMessage';
      } else if (this.isVideo(message)) {
        return 'ChatVideoMessage';
      } else if (this.isDocument(message)) {
        return 'ChatDocumentMessage';
      }
    },
    messageClasses(message) {
      const classes = ['message'];
      if (message.is_file) {
        classes.push('text-message');
      } else {
        classes.push('file-message');
      }
      if (this.user.username !== message.user.username) {
        classes.push('companion');
      }
      return classes;
    }
  }
};
</script>

<style lang="scss" scoped>
.text-message {
  align-items: flex-end;
}

.file-message {
  align-items: flex-end;
}

.message {
  color: $white;
  display: flex;
  margin: 10px 0 0 0;
  gap: 5px;
}

.companion {
  flex-direction: row-reverse;
  justify-content: flex-start;
}
</style>
