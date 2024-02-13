package com.kftc.onerelay.handler;

import io.netty.buffer.ByteBuf;
import io.netty.channel.ChannelHandlerContext;
import io.netty.channel.ChannelInboundHandlerAdapter;

public class TcpServerHandler extends ChannelInboundHandlerAdapter {
    @Override
    public void channelRead(ChannelHandlerContext ctx, Object msg) {
        if (msg instanceof ByteBuf) {
            ByteBuf in = (ByteBuf) msg;
            try {
                while (in.isReadable()) {
                    System.out.print((char) in.readByte());
                    System.out.flush();
                }
            } finally {
                in.release();
            }
        } else if (msg instanceof String) {
            // 클라이언트에서 문자열을 보낸 경우 처리
            String data = (String) msg;
            System.out.println("Received String from client: " + data);
        } else {
            System.err.println("Unsupported message type: " + msg.getClass().getName());
        }
    }

    @Override
    public void exceptionCaught(ChannelHandlerContext ctx, Throwable cause) {
        cause.printStackTrace();
        ctx.close();
    }
}
