PRAGMA foreign_keys = ON;

------------------------------------------------------------
-- Language
------------------------------------------------------------
INSERT INTO Language (language_name) VALUES
('C++'),
('C#'),
('Java'),
('JavaScript'),
('PHP'),
('Python'),
('English'),
('Portuguese'),
('German');

------------------------------------------------------------
-- Category
------------------------------------------------------------
INSERT INTO Category (category_name) VALUES
('Creational'),
('Structural'),
('Behavioral');

------------------------------------------------------------
-- Pattern
------------------------------------------------------------
INSERT INTO Pattern (pattern_name) VALUES
('Abstract Factory'),
('Builder'),
('Factory Method'),
('Prototype'),
('Singleton'),
('Adapter'),
('Bridge'),
('Composite'),
('Decorator'),
('Facade'),
('Flyweight'),
('Proxy'),
('Chain of Responsibility'),
('Command'),
('Interpreter'),
('Iterator'),
('Mediator'),
('Memento'),
('Observer'),
('State'),
('Strategy'),
('Template Method'),
('Visitor');

------------------------------------------------------------
-- Segment
------------------------------------------------------------
INSERT INTO Segment
(segment_name, display_order)
VALUES
('Open',1),
('Why',2),
('UML',3),
('Code',4),
('Mid',5),
('SWOT',6),
('Close',7),
('Full',8);

------------------------------------------------------------
-- Platform
------------------------------------------------------------
INSERT INTO Platform (platform_name) VALUES
('YouTube'),
('Vimeo'),
('GitHub'),
('Facebook'),
('X'),
('LinkedIn'),
('Instagram'),
('Website'),
('Newsletter');
