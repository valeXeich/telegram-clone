<template>
  <div class="modal-input">
    <i class="bi bi-emoji-smile"></i>
    <input type="text" placeholder="Add a caption..." :value="modelValue"
      @input="$emit('update:modelValue', $event.target.value)" />
    <button @click="$emit('addCaption')">send</button>
  </div>
</template>

<script>
export default {
  emits: ['update:modelValue', 'addCaption'],
  props: {
    previewFile: Object,
    modelValue: String
  },

};
</script>

<style lang="scss" scoped>
.modal-input {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 5px;

  i {
    font-size: 26px;
    color: rgb(170, 170, 170);
  }

  input {
    width: 100%;
    background: none;
    border: none;
    color: #fff;

    &::placeholder {
      font-family: "Segoe UI Variable";
      line-height: 21px;
      color: #8a8a8a;
    }
  }

  button {
    background-color: rgb(135, 116, 225);
    color: #fff;
    height: 2.5rem;
    padding: 0 1rem;
    border: none;
    transition: background-color .15s, color .15s;
    text-transform: uppercase;
    border-radius: 0.625rem;

    &:hover {
      background-color: #7b71c6;
    }
  }
}
</style>
