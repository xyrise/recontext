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
    <div class="tag-container">
        {#each tags as tag}
            <div class="tag"> <p>{tag}</p> </div>
        {/each}
    </div>
</div>

<style>

    .title-text {
        width: 400px;
        height: 12px;

        font-family: Nunito;
        font-style: normal;
        font-weight: bold;
        font-size: 12px;
        line-height: 97.4%;
        /* identical to box height, or 12px */
        margin: var(--bmargin);
    }

    .contentItem {
        width: 450px;
        height: 200px;
        margin: 5px;
    }

    .title {
        width: 450px;
        height: 20px;
        left: 27px;
        top: 187px;
        display: inline-flex;
        align-items: center;
        background: #FFF3E8;
        border-radius: 10px;
    }
    
    .sentence{
        margin: var(--bmargin);
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
    
    .tag-container{
        margin: var(--bmargin);
        display: flex;
        flex-direction: row 
    }

    .tag {
        border: 1px solid #FFDFC1;
        border-radius: 10px;
        
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
