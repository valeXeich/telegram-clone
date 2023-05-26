<template>
    <input :type="type" :placeholder="placeholder" :value="modelValue"
        @input="$emit('update:modelValue', $event.target.value)">
</template>

<script>
export default {
    props: {
        type: String,
        placeholder: String,
        modelValue: String
    }
}
</script>

<style lang="scss" scoped>
input {
    background: transparent;
    border: 1px solid #2f2f2f;
    padding: 10px;
    color: $white;
    border-radius: 10px;
    transition: border 0.25s;
    font-family: "Segoe UI Variable";

    &::placeholder {
        color: #7b7b7b;
    }

    &:hover {
        border: 1px solid #8774e1;

        &::placeholder {
            color: #8774e1;
        }
    }

    &:focus {
        border: 1px solid #8774e1;
    }
}</style>