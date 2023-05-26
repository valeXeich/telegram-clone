<template>
  <div class="caption" v-if="message.content">
    <p>{{ message.content }}</p>
    <ChatMessageMeta :created_at="message.created_at" :readed="message.readed" />
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
.caption {
  display: flex;
  background: rgb(118, 106, 200);
  padding: 5px;
  align-items: flex-end;
  gap: 5px;
  justify-content: space-between;
  border-radius: 0 0 5px 5px;
}
</style>
