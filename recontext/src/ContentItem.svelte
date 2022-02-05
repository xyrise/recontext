<script>
    export let title;
    export let sentences;
    export let tags;
    export let cited;
</script>

<link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Nunito%22%3E">

<div class="contentItem">
    <div class="title"><span class="title-text">{title}</span> </div> 
    <p class='sentence'>{sentences}</p>
    {#each tags as tag}
        <span class="tag"> {tag} </span>
    {/each}
</div>

<style>
    :root{
        --bgcolor: white;
        --c1: #FF9C55;
        --c1sub: #FFDAC0;
        --width: 500px;
        --height: 640px;
        --boundh: 60px;
        --boundw: 485px;
        --bradius: 10px;
        --bmargin: 5px;
    }

    .title-text {
        width: 247px;
        height: 12px;
        left: 34px;
        top: 190px;

        font-family: Nunito;
        font-style: normal;
        font-weight: bold;
        font-size: 12px;
        line-height: 97.4%;
        /* identical to box height, or 12px */

        display: flex;
        align-items: center;
    }
    .contentItem {
        width: 368px;
        height: 199px;
    }

    .title {
        width: 364px;
        height: 18px;
        left: 27px;
        top: 187px;

        background: #FFF3E8;
        border-radius: 10px;
    }
    
    .sentence{
        font-family: Nunito;
        font-style: normal;
        font-weight: normal;
        font-size: 12px;
        line-height: 125%;
        width: 334px;
        height: 75px;
        left: 35px;
        top: 211px;
        /* or 15px */

        display: flex;
        align-items: center;
    }
    
    .tag {
        position: absolute;
        width: 76px;
        height: 23px;

        font-family: Nunito;
        font-style: normal;
        font-weight: 300;
        font-size: 12px;
        line-height: 97.4%;
        /* or 12px */

        display: flex;
        align-items: center;
        text-align: center;
    }
</style>
