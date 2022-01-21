<template>
    <div class="button-container">
         <AddEntryButton v-on:add-entry="$emit('add-entry')"></AddEntryButton>
    </div>
</template>

<script>
import AddEntryButton from './AddEntryButton.vue';

export default {
    name: "EntryFooter",
    components : {
        AddEntryButton,
    }
}
</script>

<style  scoped>
    .button-container{
        margin: 5px;
    }
</style>