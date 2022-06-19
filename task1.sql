--
-- PostgreSQL database dump
--

-- Dumped from database version 9.6.6
-- Dumped by pg_dump version 9.6.6

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SET check_function_bodies = false;
SET client_min_messages = warning;
SET row_security = off;

--
-- Name: plpgsql; Type: EXTENSION; Schema: -; Owner: 
--

CREATE EXTENSION IF NOT EXISTS plpgsql WITH SCHEMA pg_catalog;


--
-- Name: EXTENSION plpgsql; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION plpgsql IS 'PL/pgSQL procedural language';


SET search_path = public, pg_catalog;

SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: cost_of_orders; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE cost_of_orders (
    numb bigint NOT NULL,
    "order" character varying(255) NOT NULL,
    cost_usd bigint,
    date date,
    cost_rur numeric(255,2)
);


ALTER TABLE cost_of_orders OWNER TO postgres;

--
-- Name: COLUMN cost_of_orders.numb; Type: COMMENT; Schema: public; Owner: postgres
--

COMMENT ON COLUMN cost_of_orders.numb IS '№';


--
-- Name: COLUMN cost_of_orders."order"; Type: COMMENT; Schema: public; Owner: postgres
--

COMMENT ON COLUMN cost_of_orders."order" IS 'pаказ №';


--
-- Name: COLUMN cost_of_orders.cost_usd; Type: COMMENT; Schema: public; Owner: postgres
--

COMMENT ON COLUMN cost_of_orders.cost_usd IS 'cтоимость, $';


--
-- Name: COLUMN cost_of_orders.date; Type: COMMENT; Schema: public; Owner: postgres
--

COMMENT ON COLUMN cost_of_orders.date IS 'cрок поставки';


--
-- Name: COLUMN cost_of_orders.cost_rur; Type: COMMENT; Schema: public; Owner: postgres
--

COMMENT ON COLUMN cost_of_orders.cost_rur IS 'стоимость, руб.';


--
-- Name: cost_of_orders cost_of_orders_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY cost_of_orders
    ADD CONSTRAINT cost_of_orders_pkey PRIMARY KEY (numb);


--
-- PostgreSQL database dump complete
--

