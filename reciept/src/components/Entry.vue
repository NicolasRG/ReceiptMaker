<template>
    <div id="container">
        <div>
            {{this.entry.item}}
        </div>
        <div>
            {{this.entry.quantity}}
        </div>
        <div>
            {{this.entry.price}}
        </div>
    </div>
</template>

<script>
export default {
    props:{
        entry: Object,
    },
    created: ()=>{
    }

}


</script>>

<style scoped>
    #container{
        background-color: burlywood;
        border: black 1px solid;
        display: flex;
        justify-content: space-around;
    }

</style>