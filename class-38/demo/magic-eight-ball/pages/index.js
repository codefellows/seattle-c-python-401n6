import Head from 'next/head';
import Header from '../components/Header';
import History from "../components/History";
import QuestionForm from "../components/QuestionForm";
import EightBall from "../components/EightBall";
import { replies } from '../data';
import { useState } from 'react';
import Link from "next/link";

export default function Home() {
    // const [reply, setReply] = useState('Ask me anything');
    const [answeredQuestions, setAnsweredQuestions] = useState([]);
    function questionAskedHandler(Question) {
        const randomReply = replies[Math.floor(Math.random() * replies.length)];

        // setReply(randomReply);
        const answeredQuestion = {
            question: Question,
            reply: randomReply,
            id: answeredQuestions.length,
        };
        setAnsweredQuestions([...answeredQuestions, answeredQuestion]);
    }

    function getLatestReply() {
        if (answeredQuestions.length === 0) {
            return 'Ask Me Anything!';
        } else {
            return answeredQuestions[answeredQuestions.length - 1].reply;
        }
    }

    return (
        <div>
            <Head>
                <title>Magic 8 Ball</title>
            </Head>
            <Header answerCount={ answeredQuestions.length }/>
            <main>
                <QuestionForm askedQuestion = { questionAskedHandler }/>
                <EightBall reply = { getLatestReply() }/>
                <History questionList = { answeredQuestions } />
            </main>
            <footer className="p-4 mt-8 bg-gray-500 test-gray-50">
                <nav className="flex items-center space-x-10 justify-left">
                    <Link href="/careers">
                        <a className="text-xl" href="careers">Careers</a>
                    </Link>
                </nav>
            </footer>
        </div>);

}
