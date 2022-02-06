<script>
    export let title;
    export let sentences;
    export let tags;
    export let cited;
    let cite = 'img/cite.png';
    let share = 'img/share.png';
    let bookmark = 'img/bookmark.png';
</script>

<link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Nunito%22%3E">

<hr>
<div class="contentItem">
    <div class="title"><span class="title-text">{title}</span> </div> 
    <p class='sentence'>{sentences}</p>
    <div class="tag-container">
        {#each tags as tag}
            <div class="tag"> <p>{tag}</p> </div>
        {/each}
    </div>
    <div class="actions">
        <span class='action'><img style='margin:auto;padding:0 0.5rem 0 0.5rem;' src={cite} alt="citation icon"> {cited} cited </span>
        <span class='action'> <img style='margin:auto;padding:0 0.5rem 0 0.5rem;' src={share} alt="sharing icon"> share </span>
        <span class='action'> <img style='margin:auto;padding:0 0.5rem 0 0.5rem;' src={bookmark} alt="bookmark icon"> bookmark </span>
    </div>
</div>

<style>

    .title-text {
        width: 400px;
        height: 16px;

        font-family: Nunito;
        font-style: normal;
        font-weight: bolder !important;
        font-size: 14px;
        line-height: 97.4%;
        /* identical to box height, or 12px */
        margin-left:10px;
        padding-top: 3px;
    }

    .contentItem {
        width: 450px;
        height: 200px;
        margin: 5px;
    }

    .title {
        width: 460px;
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
        font-size: 14px;
        line-height: 125%;
        width: 460px;
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
        border-color: var(--c1sub);
        border-style: solid;
        border-width: 2px;
        background-color: var(--bgcolor);
        border-radius: var(--bradius);
        padding:0.3rem;
        margin: 0.3rem;
    }

    .actions{
        padding-top: 12px;
        display: flex;
        flex-direction: row;
        justify-content: space-around 
    }

    .action{
        height: 23px;

        font-family: Nunito;
        font-style: normal;
        font-weight: 600;
        font-size: 16px;
        line-height: 97.4%;
        /* or 16px */

        display: flex;
        align-items: center;
    }
</style>
