//! Parser for the problem DSL.

use super::ast::*;
use super::error::ParseError;
use super::lexer::Token;

/// Parser for DSL syntax
#[derive(Debug, Clone)]
pub struct Parser {
    /// Current tokens
    tokens: Vec<Token>,
    /// Current position
    position: usize,
    /// Error messages
    errors: Vec<ParseError>,
}

impl Parser {
    /// Create a new parser
    pub fn new() -> Self {
        Self {
            tokens: Vec::new(),
            position: 0,
            errors: Vec::new(),
        }
    }

    /// Set tokens for parsing
    pub fn set_tokens(&mut self, tokens: Vec<Token>) {
        self.tokens = tokens;
        self.position = 0;
        self.errors.clear();
    }

    /// Parse tokens into AST
    pub fn parse(&mut self) -> Result<AST, ParseError> {
        self.parse_program()
    }

    /// Parse program
    fn parse_program(&mut self) -> Result<AST, ParseError> {
        let mut declarations = Vec::new();
        let mut objective = None;
        let mut constraints = Vec::new();

        while !self.is_at_end() {
            match self.current_token() {
                Token::Var | Token::Param => {
                    declarations.push(self.parse_declaration()?);
                }
                Token::Minimize | Token::Maximize => {
                    if objective.is_some() {
                        return Err(ParseError {
                            message: "Multiple objectives not supported yet".to_string(),
                            line: 0,
                            column: 0,
                        });
                    }
                    objective = Some(self.parse_objective()?);
                }
                Token::Subject => {
                    self.advance(); // consume 'subject'
                    self.expect(Token::To)?;

                    while !self.is_at_end() && !matches!(self.current_token(), Token::Eof) {
                        constraints.push(self.parse_constraint()?);
                    }
                }
                Token::NewLine | Token::Comment(_) => {
                    self.advance();
                }
                _ => {
                    return Err(ParseError {
                        message: format!("Unexpected token: {:?}", self.current_token()),
                        line: 0,
                        column: 0,
                    });
                }
            }
        }

        let obj = objective.ok_or_else(|| ParseError {
            message: "No objective function found".to_string(),
            line: 0,
            column: 0,
        })?;

        Ok(AST::Program {
            declarations,
            objective: obj,
            constraints,
        })
    }

    /// Parse declaration
    fn parse_declaration(&mut self) -> Result<Declaration, ParseError> {
        match self.current_token() {
            Token::Var => self.parse_variable_declaration(),
            Token::Param => self.parse_parameter_declaration(),
            _ => Err(ParseError {
                message: "Expected variable or parameter declaration".to_string(),
                line: 0,
                column: 0,
            }),
        }
    }

    /// Parse variable declaration
    fn parse_variable_declaration(&mut self) -> Result<Declaration, ParseError> {
        self.advance(); // consume 'var'

        let name = self.expect_identifier()?;
        let var_type = self.parse_variable_type()?;

        self.expect(Token::Semicolon)?;

        Ok(Declaration::Variable {
            name,
            var_type,
            domain: None,
            attributes: std::collections::HashMap::new(),
        })
    }

    /// Parse parameter declaration
    fn parse_parameter_declaration(&mut self) -> Result<Declaration, ParseError> {
        self.advance(); // consume 'param'

        let name = self.expect_identifier()?;
        self.expect(Token::Equal)?;
        let value = self.parse_value()?;

        self.expect(Token::Semicolon)?;

        Ok(Declaration::Parameter {
            name,
            value,
            description: None,
        })
    }

    /// Parse variable type
    fn parse_variable_type(&mut self) -> Result<super::types::VarType, ParseError> {
        use super::types::VarType;

        match self.current_token() {
            Token::Binary => {
                self.advance();
                Ok(VarType::Binary)
            }
            Token::Integer => {
                self.advance();
                Ok(VarType::Integer)
            }
            Token::Continuous => {
                self.advance();
                Ok(VarType::Continuous)
            }
            _ => Err(ParseError {
                message: "Expected variable type (binary, integer, continuous)".to_string(),
                line: 0,
                column: 0,
            }),
        }
    }

    /// Parse value
    fn parse_value(&mut self) -> Result<Value, ParseError> {
        match self.current_token() {
            Token::Number(n) => {
                let value = *n;
                self.advance();
                Ok(Value::Number(value))
            }
            Token::Boolean(b) => {
                let value = *b;
                self.advance();
                Ok(Value::Boolean(value))
            }
            Token::String(s) => {
                let value = s.clone();
                self.advance();
                Ok(Value::String(value))
            }
            Token::LeftBracket => {
                self.advance(); // consume '['
                let mut elements = Vec::new();

                while !matches!(self.current_token(), Token::RightBracket) {
                    elements.push(self.parse_value()?);

                    if matches!(self.current_token(), Token::Comma) {
                        self.advance();
                    } else {
                        break;
                    }
                }

                self.expect(Token::RightBracket)?;
                Ok(Value::Array(elements))
            }
            _ => Err(ParseError {
                message: "Expected value".to_string(),
                line: 0,
                column: 0,
            }),
        }
    }

    /// Parse objective
    fn parse_objective(&mut self) -> Result<Objective, ParseError> {
        match self.current_token() {
            Token::Minimize => {
                self.advance();
                let expr = self.parse_expression()?;
                self.expect(Token::Semicolon)?;
                Ok(Objective::Minimize(expr))
            }
            Token::Maximize => {
                self.advance();
                let expr = self.parse_expression()?;
                self.expect(Token::Semicolon)?;
                Ok(Objective::Maximize(expr))
            }
            _ => Err(ParseError {
                message: "Expected minimize or maximize".to_string(),
                line: 0,
                column: 0,
            }),
        }
    }

    /// Parse constraint
    fn parse_constraint(&mut self) -> Result<Constraint, ParseError> {
        let expression = self.parse_constraint_expression()?;
        self.expect(Token::Semicolon)?;

        Ok(Constraint {
            name: None,
            expression,
            tags: Vec::new(),
        })
    }

    /// Parse constraint expression
    fn parse_constraint_expression(&mut self) -> Result<ConstraintExpression, ParseError> {
        let left = self.parse_expression()?;

        let op = match self.current_token() {
            Token::Equal => ComparisonOp::Equal,
            Token::NotEqual => ComparisonOp::NotEqual,
            Token::Less => ComparisonOp::Less,
            Token::Greater => ComparisonOp::Greater,
            Token::LessEqual => ComparisonOp::LessEqual,
            Token::GreaterEqual => ComparisonOp::GreaterEqual,
            _ => {
                return Err(ParseError {
                    message: "Expected comparison operator".to_string(),
                    line: 0,
                    column: 0,
                })
            }
        };

        self.advance(); // consume operator
        let right = self.parse_expression()?;

        Ok(ConstraintExpression::Comparison { left, op, right })
    }

    /// Parse expression
    fn parse_expression(&mut self) -> Result<Expression, ParseError> {
        self.parse_additive()
    }

    /// Parse additive expression
    fn parse_additive(&mut self) -> Result<Expression, ParseError> {
        let mut expr = self.parse_multiplicative()?;

        while matches!(self.current_token(), Token::Plus | Token::Minus) {
            let op = match self.current_token() {
                Token::Plus => BinaryOperator::Add,
                Token::Minus => BinaryOperator::Subtract,
                _ => unreachable!(),
            };
            self.advance();
            let right = self.parse_multiplicative()?;
            expr = Expression::BinaryOp {
                op,
                left: Box::new(expr),
                right: Box::new(right),
            };
        }

        Ok(expr)
    }

    /// Parse multiplicative expression
    fn parse_multiplicative(&mut self) -> Result<Expression, ParseError> {
        let mut expr = self.parse_primary()?;

        while matches!(self.current_token(), Token::Times | Token::Divide) {
            let op = match self.current_token() {
                Token::Times => BinaryOperator::Multiply,
                Token::Divide => BinaryOperator::Divide,
                _ => unreachable!(),
            };
            self.advance();
            let right = self.parse_primary()?;
            expr = Expression::BinaryOp {
                op,
                left: Box::new(expr),
                right: Box::new(right),
            };
        }

        Ok(expr)
    }

    /// Parse primary expression
    fn parse_primary(&mut self) -> Result<Expression, ParseError> {
        match self.current_token() {
            Token::Number(n) => {
                let value = *n;
                self.advance();
                Ok(Expression::Literal(Value::Number(value)))
            }
            Token::Boolean(b) => {
                let value = *b;
                self.advance();
                Ok(Expression::Literal(Value::Boolean(value)))
            }
            Token::String(s) => {
                let value = s.clone();
                self.advance();
                Ok(Expression::Literal(Value::String(value)))
            }
            Token::Identifier(name) => {
                let var_name = name.clone();
                self.advance();

                // Check for indexing
                if matches!(self.current_token(), Token::LeftBracket) {
                    self.advance(); // consume '['
                    let mut indices = Vec::new();

                    loop {
                        indices.push(self.parse_expression()?);

                        if matches!(self.current_token(), Token::Comma) {
                            self.advance();
                        } else {
                            break;
                        }
                    }

                    self.expect(Token::RightBracket)?;
                    Ok(Expression::IndexedVar {
                        name: var_name,
                        indices,
                    })
                } else {
                    Ok(Expression::Variable(var_name))
                }
            }
            Token::LeftParen => {
                self.advance(); // consume '('
                let expr = self.parse_expression()?;
                self.expect(Token::RightParen)?;
                Ok(expr)
            }
            _ => Err(ParseError {
                message: "Expected expression".to_string(),
                line: 0,
                column: 0,
            }),
        }
    }

    /// Current token
    fn current_token(&self) -> &Token {
        self.tokens.get(self.position).unwrap_or(&Token::Eof)
    }

    /// Advance to next token
    fn advance(&mut self) {
        if !self.is_at_end() {
            self.position += 1;
        }
    }

    /// Check if at end of tokens
    fn is_at_end(&self) -> bool {
        self.position >= self.tokens.len() || matches!(self.current_token(), Token::Eof)
    }

    /// Expect specific token
    fn expect(&mut self, expected: Token) -> Result<(), ParseError> {
        if std::mem::discriminant(self.current_token()) == std::mem::discriminant(&expected) {
            self.advance();
            Ok(())
        } else {
            Err(ParseError {
                message: format!("Expected {:?}, found {:?}", expected, self.current_token()),
                line: 0,
                column: 0,
            })
        }
    }

    /// Expect identifier and return its name
    fn expect_identifier(&mut self) -> Result<String, ParseError> {
        match self.current_token() {
            Token::Identifier(name) => {
                let result = name.clone();
                self.advance();
                Ok(result)
            }
            _ => Err(ParseError {
                message: "Expected identifier".to_string(),
                line: 0,
                column: 0,
            }),
        }
    }
}

impl Default for Parser {
    fn default() -> Self {
        Self::new()
    }
}
