<template>
    <div id="container">
        <div id="delete"> 
            Delete
        </div>
        <div class="Field">
            Item
        </div>
        <div class="Field">
            Qauntity
        </div>
        <div class="Field">
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
    padding-left: 10px;
    border-bottom: white 1px solid ;
}

#delete{
        width: 50px;
        margin-left: 5px;
        left:0px;
}

.Field{
    margin-left: 40px;
    width: 20%;
    text-align: center;
}


</style>