<script>
    import Content from "./Content.svelte"
    let covid = 'img/covid.png';
    let trend = 'img/trend.png';
    let down = 'img/down.png';
    let gleft = 'img/gleft.png';
    let gright = 'img/gright.png';
    let left = 'img/Left.png';
    let right = 'img/Right.png';
</script>
<link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Nunito:200,400,600,800">

<div class='container'>
<div class='top'>
    <div class='topBar'>
        <img style='margin:auto;padding:0 0 0 0.5rem;' src={covid} alt="covid19 virus icon">
        <img style='margin:auto;padding:0 0.5rem 0 0.5rem;' src={trend} alt="heart on fire icon">
        <div class='topBarText'>
            <p> Current Keywords </p>
            <div class='tag'>
                <!-- link keywords here -->
                <!-- hardcoded tags -->
                <li class='tagIn'> Anti-vaccines </li>
                <li class='tagIn'> Freedom </li>
            </div>
        </div>
    </div>
    <div class='recon'>
        <strong style='margin:auto;padding:0 0.5rem 0 0.5rem'> ReconText </strong>
        <div class='tag'>
            <!-- link found recommending tags/keywords here -->
            <!-- hardcoded tags -->
            <li class='tagRec'> Community </li>
            <li class='tagRec'> Risky </li>
            <li class='tagRec'> Cancer </li>
            <li class='tagRec'> Regulation </li>
        </div>
    </div>
</div>
    <div class='results'>
        <strong> Related Peer-Reviewed Paper </strong>
        <Content/>
    </div>

    <div class='footer'>
        <!-- link number of pages here -->
        <img src={gleft} alt="left arrow" style="display: block;
  margin-left: auto;">
        <div style='margin:auto;'>
            <p style='margin:auto;'>1/15</p>
        </div>
        <img src={gright} alt="right arrow">
    </div>

    <div class='credit'>
        <p style='font-size:10px;padding:3px;'>© 2022 ReconText Contributors</p>
    </div>
</div>


<style>
    :root{
        --bgcolor: white;
        --c1: #FF9C55;
        --c1sub: #FFDAC0;
        --width: 500px;
        --height: 640px;
        --boundh: 70px;
        --boundw: 485px;
        --bradius: 10px;
        --bmargin: 5px;
        --arrowpadding: 20px;
    }

    p{
        margin:0.3rem 0 0 0;
    }
    strong { font-weight: bold; }

    .container{
        font-family: "Nunito",sans-serif;
        max-width: var(--width);
        max-height: var(--height);
        margin: 0;
        padding: 0;
    }
    
    .topBar{
        width: var(--boundw);
        height: var(--boundh);
        display: grid;
        grid-template-columns: 1fr 1fr 10fr 0.5fr;
        border-radius: var(--bradius);
        background-color: var(--c1);
        margin: var(--bmargin);
    }
    .topBarText{
        grid-template-rows: 1fr 2fr;
    }
    .tag{
        list-style: none;
        text-align:center;
        margin: 0rem;
        display: flex;
    }
    .tagIn{
        background-color: var(--c1sub);
        border-radius: var(--bradius);
        padding:0.3rem;
        margin: 0.3rem;
    }
    .tagRec{
        border-color: var(--c1sub);
        border-style: solid;
        border-width: 2px;
        background-color: var(--bgcolor);
        border-radius: var(--bradius);
        padding:0.3rem;
        margin: 0.3rem;
    }
    
    .recon{
        margin: 0.8rem var(--bmargin);
        display:grid;
        grid-template-columns: 1fr 12fr;
    }

    .results{
        margin: var(--bmargin);
        padding: 0 0.5rem 0 0.5rem;
    }

    .footer{
        margin: var(--bmargin) var(--bmargin) 1rem var(--bmargin);
        text-align: center;
        display: grid;
        grid-template-columns: 1fr 2fr 1fr;
    }
    .larrow, .rarrow{
        margin:auto;
        padding: 0 var(--arrowpadding);
    }

    .credit{
        height: 20px;
        width: var(--width);
        background-color: var(--c1);
        margin: auto;
        text-align: center;
    }

</style>
