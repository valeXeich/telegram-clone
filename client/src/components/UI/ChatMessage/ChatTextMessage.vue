<template>
  <div class="message-block">
    <div class="message-text">
      <p>{{ message.content }}</p>
    </div>
    <ChatMessageMeta class="message-meta" :created_at="message.created_at" :readed="message.readed" />
  </div>
</template>

<script>
import ChatMessageMeta from "./ChatMessageMeta.vue";

export default {
  props: {
    message: Object,
  },
  components: {
    ChatMessageMeta,
  },
};
</script>

<style lang="scss" scoped>
.message-block {
  align-self: center;
  background: $purpl;
  padding: 5px;
  max-width: 480px;
  border-radius: 10px;
  gap: 10px;

  .message-text {
    max-width: 480px;
    word-wrap: break-word
  }

  .message-meta {
    display: flex;
    justify-content: flex-end;

    p {
      font-size: 12px;

      i {
        font-size: 13px;
      }
    }
  }
}
</style>
