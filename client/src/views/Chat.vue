<template>
    <div class="main">
        <sidebar/>
        <div class="select-window">
            <p>Select </p>
        </div>
    </div>
</template>

<script>
import Sidebar from '@/components/Sidebar.vue';

export default {
    components: {
        Sidebar
    }
}
</script>

<style lang="scss" scoped>

.main {
    display: flex;
    width: 100%;
}

.select-window {
    background-image: url(https://web.telegram.org/a/chat-bg-pattern-dark.ad38368a9e8140d0ac7d.png);
    background-color: black;
    width: 100%;
}

</style>