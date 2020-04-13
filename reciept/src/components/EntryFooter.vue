<template>
    <div>
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

</style>