<template>
  <div class="message">
    <div class="message-document">
      <div class="file-icon">
        <i class="bi bi-file-earmark-fill"></i>
      </div>
      <div class="file-info">
        <p class="file-name">{{ message.file_name }}</p>
        <p class="file-size">{{ humanFileSize(message.size) }}</p>
      </div>
    </div>
    <ChatMessageMeta v-if="!message.content" class="message-meta" :created_at="message.created_at"
      :readed="message.readed" />
    <ChatMesssageCaption :message="message" v-else />
  </div>
</template>

<script>
import ChatMessageMeta from './ChatMessageMeta.vue';
import ChatMesssageCaption from './ChatMesssageCaption.vue';
import { humanFileSize } from '@/utils/humanFileSize';

export default {
  props: {
    message: Object
  },
  components: {
    ChatMessageMeta,
    ChatMesssageCaption
  },
  methods: {
    humanFileSize
  }
}
</script>

<style lang="scss" scoped>
.message {
  background: rgb(118, 106, 200);
  border-radius: 10px;
  padding: 10px;
  display: flex;
  flex-direction: column;

  .message-meta {
    display: flex;
    justify-content: flex-end;
  }
}

.message-document {
  display: flex;
  align-items: center;
  gap: 5px;

  .file-icon {
    font-size: 26px;
    background-color: #007dd2;
    padding: 10px;
    border-radius: 50%;
  }

  .file-info {
    .file-name {
      font-size: 18px;
      line-height: 1.5rem;
    }

    .file-size {
      font-size: 14px;
      color: #aaaa;
      line-height: 1rem;
    }
  }
}
</style>