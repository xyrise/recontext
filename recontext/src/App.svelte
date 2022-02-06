<script>
    import { onMount } from 'svelte';
    import Content from "./Content.svelte"
    import { Readability } from '@mozilla/readability';
    import {retext} from 'retext';
    import retextPos from 'retext-pos';
    import retextKeywords from 'retext-keywords';
    import {toString} from 'nlcst-to-string';
import { get } from 'svelte/store';
import ContentItem from './ContentItem.svelte';

    let covid = 'img/covid.png';
    let trend = 'img/trend.png';
    let down = 'img/down.png';
    let gleft = 'img/gleft.png';
    let gright = 'img/gright.png';
    let left = 'img/Left.png';
    let right = 'img/Right.png';
    
    async function getKeywords() {

        function modifyDOM() {
            return document.body.innerHTML;
        }

        let result = await chrome.tabs.executeScript({
            code: '(' + modifyDOM + ')();' 
            }, (results) => {
                let text;
                console.log('Popup script:')
                console.log(results[0]);
                var doc = document.implementation.createHTMLDocument("New Document");
                doc.body.parentElement.innerHTML = results[0];    
                var article = new Readability(doc).parse();
                console.log("next line is content");
                console.log(article.textContent);
                text = article.textContent;

                return retext()
                    .use(retextPos) // Make sure to use `retext-pos` before `retext-keywords`.
                    .use(retextKeywords)
                    .process(text)
                    .then(
                        (file) => {
                            let url = new URL("http://0.0.0.0:80");
                            let params = new URLSearchParams();
                            params.append('max',5);
                            let keywords = [];

                            console.log('Keywords:');
                            file.data.keywords.forEach((keyword) => {
                                keywords.push(toString(keyword.matches[0].node));
                                params.append('key',toString(keyword.matches[0].node));
                                console.log(keyword);
                            });
                            url.search = params.toString();
                            return url;
                    }).then((url) => {return url});
            });
        console.log(result);
        return result;
    }

    async function getResults() {
        let url = await getKeywords();
        const res = await fetch(url, { method: 'get' });
		const json = await res.json();
        console.log(json);
		if (res.ok) {
			return json;
		} else {
			throw new Error(text);
		}
	}

    let promise = getResults();
    
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
        {#await promise}
            <p>...waiting</p>
        {:then results}
            <Content results={results}/>
        {:catch error}
            <p style="color: red">{error.message}</p>
        {/await}
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
