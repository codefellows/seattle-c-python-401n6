export default function Header( { answerCount } ) {
    return(
        <header className="flex items-center p-4 justify-between bg-gray-500 text-gray-50">
            <h1 className="text-4xl">Magic 8 Ball</h1>
            <p>{answerCount} questions answered</p>
        </header>
    );
}
