//! Lexical analysis for the problem DSL.

use super::error::ParseError;
use std::fmt;

/// Token types
#[derive(Debug, Clone, PartialEq)]
pub enum Token {
    // Literals
    Number(f64),
    String(String),
    Boolean(bool),
    Identifier(String),

    // Keywords
    Var,
    Param,
    Constraint,
    Minimize,
    Maximize,
    Subject,
    To,
    Binary,
    Integer,
    Continuous,
    In,
    ForAll,
    Exists,
    Sum,
    Product,
    If,
    Then,
    Else,
    Let,
    Define,
    Macro,
    Import,
    From,
    As,
    Domain,
    Range,
    Symmetry,
    Hint,

    // Operators
    Plus,
    Minus,
    Times,
    Divide,
    Power,
    Equal,
    NotEqual,
    Less,
    Greater,
    LessEqual,
    GreaterEqual,
    And,
    Or,
    Not,
    Implies,
    Mod,
    Xor,

    // Delimiters
    LeftParen,
    RightParen,
    LeftBracket,
    RightBracket,
    LeftBrace,
    RightBrace,
    Comma,
    Semicolon,
    Colon,
    Arrow,
    Dot,
    DoubleDot,
    Pipe,

    // Special
    Eof,
    NewLine,
    Comment(String),
}

impl fmt::Display for Token {
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        match self {
            Token::Number(n) => write!(f, "{}", n),
            Token::String(s) => write!(f, "\"{}\"", s),
            Token::Boolean(b) => write!(f, "{}", b),
            Token::Identifier(id) => write!(f, "{}", id),
            Token::Var => write!(f, "var"),
            Token::Param => write!(f, "param"),
            Token::Constraint => write!(f, "constraint"),
            Token::Minimize => write!(f, "minimize"),
            Token::Maximize => write!(f, "maximize"),
            Token::Subject => write!(f, "subject"),
            Token::To => write!(f, "to"),
            Token::Binary => write!(f, "binary"),
            Token::Integer => write!(f, "integer"),
            Token::Continuous => write!(f, "continuous"),
            Token::In => write!(f, "in"),
            Token::ForAll => write!(f, "forall"),
            Token::Exists => write!(f, "exists"),
            Token::Sum => write!(f, "sum"),
            Token::Product => write!(f, "product"),
            Token::If => write!(f, "if"),
            Token::Then => write!(f, "then"),
            Token::Else => write!(f, "else"),
            Token::Let => write!(f, "let"),
            Token::Define => write!(f, "define"),
            Token::Macro => write!(f, "macro"),
            Token::Import => write!(f, "import"),
            Token::From => write!(f, "from"),
            Token::As => write!(f, "as"),
            Token::Domain => write!(f, "domain"),
            Token::Range => write!(f, "range"),
            Token::Symmetry => write!(f, "symmetry"),
            Token::Hint => write!(f, "hint"),
            Token::Plus => write!(f, "+"),
            Token::Minus => write!(f, "-"),
            Token::Times => write!(f, "*"),
            Token::Divide => write!(f, "/"),
            Token::Power => write!(f, "^"),
            Token::Equal => write!(f, "=="),
            Token::NotEqual => write!(f, "!="),
            Token::Less => write!(f, "<"),
            Token::Greater => write!(f, ">"),
            Token::LessEqual => write!(f, "<="),
            Token::GreaterEqual => write!(f, ">="),
            Token::And => write!(f, "&&"),
            Token::Or => write!(f, "||"),
            Token::Not => write!(f, "!"),
            Token::Implies => write!(f, "=>"),
            Token::Mod => write!(f, "%"),
            Token::Xor => write!(f, "xor"),
            Token::LeftParen => write!(f, "("),
            Token::RightParen => write!(f, ")"),
            Token::LeftBracket => write!(f, "["),
            Token::RightBracket => write!(f, "]"),
            Token::LeftBrace => write!(f, "{{"),
            Token::RightBrace => write!(f, "}}"),
            Token::Comma => write!(f, ","),
            Token::Semicolon => write!(f, ";"),
            Token::Colon => write!(f, ":"),
            Token::Arrow => write!(f, "->"),
            Token::Dot => write!(f, "."),
            Token::DoubleDot => write!(f, ".."),
            Token::Pipe => write!(f, "|"),
            Token::Eof => write!(f, "EOF"),
            Token::NewLine => write!(f, "\\n"),
            Token::Comment(c) => write!(f, "// {}", c),
        }
    }
}

/// Tokenize source code
pub fn tokenize(source: &str) -> Result<Vec<Token>, ParseError> {
    let mut tokens = Vec::new();
    let mut chars = source.chars().peekable();
    let mut line = 1;
    let mut column = 1;

    while let Some(&ch) = chars.peek() {
        match ch {
            // Whitespace
            ' ' | '\t' | '\r' => {
                chars.next();
                column += 1;
            }
            '\n' => {
                chars.next();
                tokens.push(Token::NewLine);
                line += 1;
                column = 1;
            }

            // Numbers
            '0'..='9' => {
                let mut number = String::new();
                while let Some(&ch) = chars.peek() {
                    if ch.is_ascii_digit() || ch == '.' {
                        number.push(chars.next().unwrap());
                        column += 1;
                    } else {
                        break;
                    }
                }
                let value = number.parse::<f64>().map_err(|_| ParseError {
                    message: format!("Invalid number: {}", number),
                    line,
                    column,
                })?;
                tokens.push(Token::Number(value));
            }

            // Strings
            '"' => {
                chars.next(); // consume opening quote
                column += 1;
                let mut string = String::new();
                while let Some(ch) = chars.next() {
                    column += 1;
                    if ch == '"' {
                        break;
                    } else if ch == '\\' {
                        if let Some(escaped) = chars.next() {
                            column += 1;
                            match escaped {
                                'n' => string.push('\n'),
                                't' => string.push('\t'),
                                'r' => string.push('\r'),
                                '\\' => string.push('\\'),
                                '"' => string.push('"'),
                                _ => {
                                    string.push('\\');
                                    string.push(escaped);
                                }
                            }
                        }
                    } else {
                        string.push(ch);
                    }
                }
                tokens.push(Token::String(string));
            }

            // Identifiers and keywords
            'a'..='z' | 'A'..='Z' | '_' => {
                let mut identifier = String::new();
                while let Some(&ch) = chars.peek() {
                    if ch.is_alphanumeric() || ch == '_' {
                        identifier.push(chars.next().unwrap());
                        column += 1;
                    } else {
                        break;
                    }
                }

                let token = match identifier.as_str() {
                    "var" => Token::Var,
                    "param" => Token::Param,
                    "constraint" => Token::Constraint,
                    "minimize" => Token::Minimize,
                    "maximize" => Token::Maximize,
                    "subject" => Token::Subject,
                    "to" => Token::To,
                    "binary" => Token::Binary,
                    "integer" => Token::Integer,
                    "continuous" => Token::Continuous,
                    "in" => Token::In,
                    "forall" => Token::ForAll,
                    "exists" => Token::Exists,
                    "sum" => Token::Sum,
                    "product" => Token::Product,
                    "if" => Token::If,
                    "then" => Token::Then,
                    "else" => Token::Else,
                    "let" => Token::Let,
                    "define" => Token::Define,
                    "macro" => Token::Macro,
                    "import" => Token::Import,
                    "from" => Token::From,
                    "as" => Token::As,
                    "domain" => Token::Domain,
                    "range" => Token::Range,
                    "symmetry" => Token::Symmetry,
                    "hint" => Token::Hint,
                    "true" => Token::Boolean(true),
                    "false" => Token::Boolean(false),
                    "xor" => Token::Xor,
                    _ => Token::Identifier(identifier),
                };
                tokens.push(token);
            }

            // Comments
            '/' => {
                chars.next();
                column += 1;
                if chars.peek() == Some(&'/') {
                    chars.next();
                    column += 1;
                    let mut comment = String::new();
                    while let Some(&ch) = chars.peek() {
                        if ch == '\n' {
                            break;
                        }
                        comment.push(chars.next().unwrap());
                        column += 1;
                    }
                    tokens.push(Token::Comment(comment));
                } else {
                    tokens.push(Token::Divide);
                }
            }

            // Operators and delimiters
            '+' => {
                chars.next();
                column += 1;
                tokens.push(Token::Plus);
            }
            '-' => {
                chars.next();
                column += 1;
                if chars.peek() == Some(&'>') {
                    chars.next();
                    column += 1;
                    tokens.push(Token::Arrow);
                } else {
                    tokens.push(Token::Minus);
                }
            }
            '*' => {
                chars.next();
                column += 1;
                tokens.push(Token::Times);
            }
            '^' => {
                chars.next();
                column += 1;
                tokens.push(Token::Power);
            }
            '%' => {
                chars.next();
                column += 1;
                tokens.push(Token::Mod);
            }
            '=' => {
                chars.next();
                column += 1;
                if chars.peek() == Some(&'=') {
                    chars.next();
                    column += 1;
                    tokens.push(Token::Equal);
                } else if chars.peek() == Some(&'>') {
                    chars.next();
                    column += 1;
                    tokens.push(Token::Implies);
                } else {
                    return Err(ParseError {
                        message: "Expected '==' or '=>'".to_string(),
                        line,
                        column,
                    });
                }
            }
            '!' => {
                chars.next();
                column += 1;
                if chars.peek() == Some(&'=') {
                    chars.next();
                    column += 1;
                    tokens.push(Token::NotEqual);
                } else {
                    tokens.push(Token::Not);
                }
            }
            '<' => {
                chars.next();
                column += 1;
                if chars.peek() == Some(&'=') {
                    chars.next();
                    column += 1;
                    tokens.push(Token::LessEqual);
                } else {
                    tokens.push(Token::Less);
                }
            }
            '>' => {
                chars.next();
                column += 1;
                if chars.peek() == Some(&'=') {
                    chars.next();
                    column += 1;
                    tokens.push(Token::GreaterEqual);
                } else {
                    tokens.push(Token::Greater);
                }
            }
            '&' => {
                chars.next();
                column += 1;
                if chars.peek() == Some(&'&') {
                    chars.next();
                    column += 1;
                    tokens.push(Token::And);
                } else {
                    return Err(ParseError {
                        message: "Expected '&&'".to_string(),
                        line,
                        column,
                    });
                }
            }
            '|' => {
                chars.next();
                column += 1;
                if chars.peek() == Some(&'|') {
                    chars.next();
                    column += 1;
                    tokens.push(Token::Or);
                } else {
                    tokens.push(Token::Pipe);
                }
            }
            '(' => {
                chars.next();
                column += 1;
                tokens.push(Token::LeftParen);
            }
            ')' => {
                chars.next();
                column += 1;
                tokens.push(Token::RightParen);
            }
            '[' => {
                chars.next();
                column += 1;
                tokens.push(Token::LeftBracket);
            }
            ']' => {
                chars.next();
                column += 1;
                tokens.push(Token::RightBracket);
            }
            '{' => {
                chars.next();
                column += 1;
                tokens.push(Token::LeftBrace);
            }
            '}' => {
                chars.next();
                column += 1;
                tokens.push(Token::RightBrace);
            }
            ',' => {
                chars.next();
                column += 1;
                tokens.push(Token::Comma);
            }
            ';' => {
                chars.next();
                column += 1;
                tokens.push(Token::Semicolon);
            }
            ':' => {
                chars.next();
                column += 1;
                tokens.push(Token::Colon);
            }
            '.' => {
                chars.next();
                column += 1;
                if chars.peek() == Some(&'.') {
                    chars.next();
                    column += 1;
                    tokens.push(Token::DoubleDot);
                } else {
                    tokens.push(Token::Dot);
                }
            }

            _ => {
                return Err(ParseError {
                    message: format!("Unexpected character: '{}'", ch),
                    line,
                    column,
                });
            }
        }
    }

    tokens.push(Token::Eof);
    Ok(tokens)
}
