<template>
  <div class="message-image">
    <div class="relative">
      <img :class="[
        message.content ? 'half-rounded' : 'full-rounded',
        'image',
      ]" :src="message.file" alt="image" />
      <ChatMessageMeta v-if="!message.content" class="message-meta" :created_at="message.created_at"
        :readed="message.readed" />
    </div>
    <ChatMesssageCaption v-if="message.content" :message="message" />
  </div>
</template>

<script>
import ChatMesssageCaption from "./ChatMesssageCaption.vue";
import ChatMessageMeta from "./ChatMessageMeta.vue";

export default {
  props: {
    message: Object,
  },
  components: {
    ChatMesssageCaption,
    ChatMessageMeta,
  },
};
</script>

<style lang="scss" scoped>
.message-image {
  cursor: pointer;

  .image {
    max-height: 384px;
    max-width: 480px;
  }

  .message-meta {
    position: absolute;
    background: rgba(0, 0, 0, 0.2);
    border-radius: 0.625rem;
    padding: 3px;
    bottom: 0.25rem;
    right: 0.25rem;

    p {
      font-size: 14px;
    }
  }
}
</style>
