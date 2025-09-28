use std::{convert::Infallible, time::Duration};

use axum::{
    extract::{self},
    response::{
        sse::{Event, Sse},
        IntoResponse, Response,
    },
};
use futures::stream;
use tokio_stream::StreamExt;

#[derive(serde::Deserialize)]
pub struct PingQuery {
    stream: Option<bool>,
}

pub async fn ping_handler(extract::Query(query): extract::Query<PingQuery>) -> Response {
    let response = format!("pong (from baml v{})", env!("CARGO_PKG_VERSION"));

    match query.stream {
        Some(true) => {
            // Create an endless stream of "pong" messages
            let stream = stream::iter(0..)
                .map(move |i| {
                    Ok::<_, Infallible>(Event::default().data(format!("{response}: seq {i}")))
                })
                .throttle(Duration::from_millis(500));

            Sse::new(stream).into_response()
        }
        _ => format!("{response}\n").into_response(),
    }
}
