<template>
    <div class="sidebar">
        <TheSearch/>
        <div class="scroll">
            <TheRoomList/>
        </div>
    </div>
</template>

<script>
import TheRoomList from './UI/TheRoomList.vue';
import TheSearch from './UI/TheSearch.vue';

export default {
    components: {
        TheRoomList,
        TheSearch
    },
}
</script>

<style lang="scss" scoped>
    .sidebar {
        min-width: 430px;
        min-height: 100vh;
        color: #fff;
        border-right: 1px solid #555;
        background: rgb(33,33,33)
    }

    .scroll {
        max-height: calc(100vh - 50px); /* Adjust this value to account for other elements on your page */
        overflow-y: auto;
        &::-webkit-scrollbar {
            width: 5px;
        }

        &::-webkit-scrollbar-track {
            background: transparent; 
        }
            
        &::-webkit-scrollbar-thumb {
            background: #979A9F;
            border-radius: 9999px;
        }

        &::-webkit-scrollbar-thumb:hover {
            background: #555; 
        }
    }
</style>