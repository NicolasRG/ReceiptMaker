<template>
    <div id="container">
        <div id="delete"> 
            Delete
        </div>
        <div>
            Item
        </div>
        <div>
            Qauntity
        </div>
        <div>
            Price
        </div>
    </div>
</template>

<script>
export default {
    
}
</script>

<style scoped>

#container{
    display : flex;
    flex-direction: row;
    flex-wrap: nowrap;
    justify-content: space-around;
    background-color: white;
    border: black 1px solid;
}

#delete{
        max-width: 100px;
        left:0px;
}


</style>